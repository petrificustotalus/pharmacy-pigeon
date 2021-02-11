from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from models import Drug
from app import app


# startpage route - localhost:5000/blog/
@app.route("/")
def home():

    if request.method == 'POST':
        drugname = request.args.get('drugname')

        return redirect(url_for('search_results', drugname=drugname))

    return render_template('home.jinja2')


# searchresults route - localhost:5000/<slug>/
@app.route("/<slug>")
def search_results(drugname):
    drug = Drug.query.filter(Drug.name==drugname).first()
    return render_template('search_results.html', drug=drug)