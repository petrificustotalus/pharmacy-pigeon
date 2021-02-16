from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '32f0e62f7cba092e8707475e1f1a0c60'

db = SQLAlchemy(app)
