from flask import render_template, request, redirect, url_for, Response
from medivisor import app, db
from medivisor.models import Druginfo
from medivisor.forms import SearchForm
import json

drugs = ["Allertec", "Ketonal", "Ketoprofen"]


@app.route("/_autocomplete", methods=["GET"])
def autocomplete():
    return Response(json.dumps(drugs), mimetype="application/json")


@app.route("/base", methods=["GET"])
def base():
    return render_template("base.jinja2")


@app.route("/", methods=["GET"])
def home():
    form = SearchForm()
    return render_template("home.jinja2", form=form)


@app.route("/search_results/<drugname>", methods=["GET"])
def search_results(drugname):
    drug = Druginfo.query.filter(Druginfo.name == drugname).first()
    searchform = SearchForm()
    if drug:
        return render_template(
            "search_results.html", drug=drug, searchform=searchform
        )
    else:
        return redirect(url_for("error_page"))


# this route gets SearchForm, takes drugname from it, and pass it to search_results
@app.route("/search_results_redirection", methods=["POST"])
def search_results_redirection():
    drugname = request.form.get("drugname").lower()
    return redirect(url_for("search_results", drugname=drugname))


@app.route("/error-page")
def error_page():
    return render_template("error_page.html")


@app.route("/informacja-o-przetwarzaniu-danych-osobowych")
def rodo():
    return render_template("rodo.html")