from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from forms import SearchForm, ClientDataForm


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
def search_results(drugname):
    drug = Druginfo.query.filter(Druginfo.name == drugname).first()
    form = ClientDataForm()
    if drug:
        return render_template("search_results.html", drug=drug, form=form)
    else:
        return redirect(url_for('error_page'))


@app.route("/order/<drugitem_id>", methods=["POST"])
def add_order(drugitem_id):
    # this part adds new client to Client table (it supposed to verify if the client doesn't already exist)
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")

    try:
        client = Client(
            name=name, surname=surname, email=email, phone=phone, address=address
        )
        db.session.add(client)
        db.session.commit()
    except:
        print("Very long traceback")
    # this part adds order to the order table
    order = Order(client_id=client.id, drugitem_id=drugitem_id)
    db.session.add(order)
    db.session.commit()
    return redirect(url_for("confirmation", order_id=order.id))

@app.route("/confirmation/<order_id>")
def confirmation(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    return render_template("confirmation.html", order=order)

@app.route("/error-page")
def error_page():
    return render_template("error_page.html")

@app.route("/informacja-o-przetwarzaniu-danych-osobowych")
def rodo():
    return render_template("rodo.html")