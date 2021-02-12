from flask import render_template, request, redirect, url_for
from app import app, db
from models import Drug
from forms import SearchForm


# startpage route - localhost:5000/blog/
@app.route("/", methods=['POST', 'GET'])
def home():
    form = SearchForm()

    if request.method == 'POST':
        # city = request.form.get('city')
        drugname = request.form.get('drugname')
        print(drugname)
        print("funkcja url_for zwraca:")
        print(url_for('search_results', drugname=drugname))
        return redirect(url_for('search_results', drugname=drugname))

    return render_template('home.jinja2', form=form)


# searchresults route - localhost:5000/<slug>/
@app.route("/search_results/<drugname>")
def search_results(drugname):  # will take 'drugname'
    print("jestem w funkcji search_results")
    print(drugname)
    drug = Drug.query.filter(Drug.name==drugname).first()
    return render_template('search_results.html', drug=drug) 