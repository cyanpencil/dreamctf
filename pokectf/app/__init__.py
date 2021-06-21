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
from flask_wtf.csrf import CSRFProtect

import datetime
import os
import time
import functools

################################
#########   GLOBALS   ##########
################################

MAX_SCORE = 100
MIN_SCORE = 20
RATE_SCORE = 2

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY', 'for dev')
app.config["SECURITY_PASSWORD_SALT"] = 'xxxxxxxxxxx'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
app.config["FIRST_BLOOD_WEBHOOK"] = "https://discord.com/api/xxxxxxxx"
app.config["SOLVE_WEBHOOK"] = "https://discord.com/api/xxxxxxxx"
#app.config["PREFERRED_URL_SCHEME"] = 'https' #decomment for HTTPS
CSRFProtect(app)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#########   stuff for new frontend   ##########
################################
from . import curtains, grimes, color
app.jinja_env.globals.update(print_curtains=curtains.print_curtains)
app.jinja_env.globals.update(gen_colors=color.gen_colors)
app.jinja_env.globals.update(gg=grimes.gg)

from . import routes
