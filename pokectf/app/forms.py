from flask import Flask, render_template, redirect, url_for, flash, session, abort, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import desc
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Length


################################
###########  FORMS   ###########
################################

class LoginForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ChallengeForm(FlaskForm):
    flag = StringField('The Flag', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Send')

class RegistrationForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=50)])
    password_again = PasswordField('Password again',
                                   validators=[DataRequired(), EqualTo('password'), Length(min=1, max=50)])
    submit = SubmitField('Register')
