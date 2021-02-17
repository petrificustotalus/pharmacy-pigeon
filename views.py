from flask import render_template, request, redirect, url_for
from app import app, db
from models import Druginfo, DrugItem, Client
from forms import SearchForm, ClientDataForm, ReservationForm


# startpage route - localhost:5000/blog/
@app.route("/", methods=["POST", "GET"])
def home():
    form = SearchForm()

    if request.method == "POST":
        # city = request.form.get('city')
        drugname = request.form.get("drugname")
        return redirect(url_for("search_results", drugname=drugname))

    return render_template("home.jinja2", form=form)


# searchresults route - localhost:5000/<slug>/
@app.route("/search_results/<drugname>", methods=["POST", "GET"])
def search_results(drugname):  # will take 'drugname'
    drug = Druginfo.query.filter(Druginfo.name == drugname).first()
    form = ClientDataForm()
    reservation_form = ReservationForm()
    # if request.method == "POST":
    #     name = request.form.get("name")
    #     surname = request.form.get("surname")
    #     email = request.form.get("email")
    #     phone = request.form.get("phone")
    #     address = request.form.get("address")

    #     try:
    #         client = Client(
    #             name=name, surname=surname, email=email, phone=phone, address=address
    #         )
    #         db.session.add(client)
    #         db.session.commit()
    #     except:
    #         print("Very long traceback")
    #     return redirect(url_for("home"))

    return render_template("search_results.html", drug=drug, form=form, reservation_form=reservation_form)
