import os
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_session import Session
from apscheduler.schedulers.background import BackgroundScheduler
from config import Config

# nie wiem czy te app.config powinny być wewnątrz tej funkcji ale wydaje mi się że tak
create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
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
    # SESSION_SQLALCHEMY
    # SESSION_SQLALCHEMY_TABLE
    db = SQLAlchemy(app)
    scheduler = BackgroundScheduler()
    with app.app_context():
        # rozumiem że tu powinna być funkcja reservation_annulation_scheduler() z utils.py
    return scheduler, app, mail, db
