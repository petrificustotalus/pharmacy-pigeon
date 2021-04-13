import os
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_session import Session
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# app.config['SCHEDULER_API_ENABLED'] = True
app.config['SECRET_KEY'] = '32f0e62f7cba092e8707475e1f1a0c60'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('USER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('PASSWORD_EMAIL')
mail = Mail(app)
# configure sessions:
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)