#
# Copyright (c) 2019 Andrea Fioraldi <andreafioraldi@gmail.com>
# This code is under the BSD 2-clause license
#
# Code inspired by https://github.com/abdesslem/CTF (Copyright (c) 2015 Amri Abdesslem)
#

from flask import Flask, render_template, redirect, url_for, flash, session, abort, request
from flask_security import Security
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import desc
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Required, Length, EqualTo, Email, Length
from flask_wtf.csrf import CsrfProtect

import datetime
import os
import time
import functools

from . import app, db, login_manager
from .models import User, Challenges, user_score
from .forms import *
from .webhooks import *

################################
##########  ROUTES   ###########
################################

@login_manager.user_loader
def load_user(user_id):
    """User loader callback for Flask-Login."""
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/challenges')
def challenges():
    challenges = Challenges.query.all()
    return render_template('challenges.html', challenges=challenges)

@app.route('/scoreboard')
def scoreboard():
    users = User.query.filter(User.username!='admin').all()
    def custom_order(x, y):
        rx = user_score(x)
        ry = user_score(y)
        if rx != ry: return rx - ry
        tx = time.mktime(x.lastSubmit.timetuple()) if x.lastSubmit else 0
        ty = time.mktime(y.lastSubmit.timetuple()) if y.lastSubmit else 0
        return int(ty - tx)
    l = sorted(list(users), key=functools.cmp_to_key(custom_order), reverse=True)
    ranking = -1 if not current_user.is_authenticated else int(l.index(current_user)) + 1
    return render_template('scoreboard.html', users=l, ranking=ranking)

@app.route('/challenge/<challenge_name>',methods=["GET","POST"])
def challenge(challenge_name):
    form = ChallengeForm(request.form)
    challenge = Challenges.query.filter_by(name=challenge_name).first()
    
    if form.validate_on_submit() and challenge.flag == form.flag.data and User.is_authenticated:
        user = User.query.filter_by(username=current_user.username).first()
        if str(challenge.id) in user.solved.split(","):
            return "Ehi! You can't submit two times the same flag!"
        user.solved = user.solved + ',' + str(challenge.id)
        user.lastSubmit = datetime.datetime.utcnow()
        name = user.username
        chal_name = challenge.name
        if challenge.solves == "0":
            first_blood_hook(name, chal_name)
        else:
            solve_hook(name, chal_name)
        challenge.solves = str(int(challenge.solves) +1)
        db.session.commit()
        return "Well done, the flag is correct."
    elif form.validate_on_submit() and challenge.flag != form.flag.data and User.is_authenticated:
        return 'Wrong Flag!'
    
    return render_template('challenge.html',form=form, challenge=challenge )

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.login.data).first()
        if user is not None:
            return 'Username already exists.'
        user = User(username=form.login.data,
                       email="foo@bar.xyz",
                       password=form.password.data,
                       solved='')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.login.data).first()
        if user is None or not user.verify_password(form.password.data):
            return 'Invalid username or password'
         
        login_user(user)
        return redirect(url_for('index'))
    
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))