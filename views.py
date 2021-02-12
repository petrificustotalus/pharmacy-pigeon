from flask import render_template
from app import app


# startpage route - localhost:5000/blog/
@app.route("/")
def home():
    return render_template('home.jinja2')


# searchresults route - localhost:5000/<slug>/
@app.route("/search_results")
def search_results():  # will take 'drugname'
    # drug = Drug.query.filter(Drug.name==drugname).first()
    return render_template('search_results.html')  # drug=drug