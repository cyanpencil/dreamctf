from flask import Flask, render_template, redirect, url_for, flash, session, abort, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import desc
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from . import db, app


################################
##########   MODELS   ##########
################################

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80))
    password_hash = db.Column(db.String(120))
    solved = db.Column(db.String(400))
    lastSubmit = db.Column(db.DateTime)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

class Challenges(db.Model):
    __tablename__ = 'challenges'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    category = db.Column(db.String(60))
    info = db.Column(db.String(1000))
    score = db.Column(db.String(20))
    flag = db.Column(db.String(80))
    solves = db.Column(db.String(20))

    def __repr__(self):
        return '<Challenges %r>' % self.name


def user_score(user):
    solved = user.solved.split(",")
    score = 0
    for c in solved:
        if len(c) == 0: continue
        q = Challenges.query.get(int(c))
        if q is None: continue
        score += int(q.score)
    return score

@app.context_processor
def utility_processor():
    return dict(user_score=user_score)
