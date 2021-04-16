from flask import render_template, request, redirect, url_for, flash, Response, session
from medivisor import app, db
from medivisor.models import Druginfo, DrugItem, Client, Pharmacy, Order
from medivisor.forms import SearchForm, ClientDataForm
import json

drugs = ["Allertec", "Ketonal", "Ketoprofen"]

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(drugs), mimetype='application/json')

@app.route("/", methods=["GET", "POST"])
def home():
    form = SearchForm()
    return render_template("home.jinja2", form=form)

# searchresults route - localhost:5000/<slug>/ wouldn't be better?
@app.route("/search_results/<drugname>", methods=["GET"])
def search_results(drugname):
    drug = Druginfo.query.filter(Druginfo.name == drugname).first()
    searchform = SearchForm()
    if drug:
        form = ClientDataForm()
        return render_template("search_results.html", drug=drug, form=form, searchform=searchform)
    else:
        return redirect(url_for('error_page'))

# this route gets SearchForm, takes drugname from it, and pass it to search_results
@app.route("/search_results_redirection", methods=["POST"])
def search_results_redirection():
    drugname = request.form.get("drugname").lower()
    return redirect(url_for("search_results", drugname=drugname))


def special_order_number_generator():
    order_number = 100000
    while order_number < 1000000:
        yield order_number
        order_number += 1
    # sprawdzić czy da się if order_number < 100000:
    # yield order_number
    # order_number += 1
    # else:
    # order_number = 100000

g = special_order_number_generator()

def update_drug_quantity(drugitem_id, quantity):
    drugitem = DrugItem.query.filter(DrugItem.id == drugitem_id).first()
    old_quantity = drugitem.quantity
    new_quantity = old_quantity - quantity
    drugitem.quantity = new_quantity
    db.session.commit()

@app.route("/order/<drugitem_id>", methods=["POST"])
def add_order(drugitem_id):
    # this part adds new client to Client table (it supposed to verify if the client doesn't already exist)
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    quantity = int(request.form.get("quantity"))
    special_order_number = next(g)

    try:
        client = Client(
            name=name, surname=surname, email=email, phone=phone, address=address
        )
        db.session.add(client)
        db.session.commit()
    except:
        print("Very long traceback")
    # this part adds order to the order table
    order = Order(client_id=client.id, drugitem_id=drugitem_id, quantity=quantity, special_order_number=special_order_number)
    db.session.add(order)
    db.session.commit()
    # this part update drug quantity in drug_item table
    update_drug_quantity(drugitem_id, quantity)
    return redirect(url_for("confirmation", special_order_number=special_order_number))


@app.route("/cart_orders_adding", methods=["POST"])
def add_cart_orders():
    # this part adds new client to Client table (it supposed to verify if the client doesn't already exist)
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    special_order_number = next(g)

    try:
        client = Client(
            name=name, surname=surname, email=email, phone=phone, address=address
        )
        db.session.add(client)
        db.session.commit()
    except:
        print("Very long traceback")

    # this part adds order to the orders table
    for cart_item in session["cart"]:
        drugitem_id = cart_item['drug_id']
        quantity = cart_item['quantity']
        order = Order(client_id=client.id, drugitem_id=drugitem_id, quantity=quantity, special_order_number=special_order_number)
        db.session.add(order)
        db.session.commit()
        update_drug_quantity(drugitem_id, quantity)
    return redirect(url_for("confirmation", special_order_number=special_order_number))
    

@app.route("/confirmation/<special_order_number>")
def confirmation(special_order_number):
    orders = Order.query.filter(Order.special_order_number == special_order_number).all()
    return render_template("confirmation.html", orders=orders)

@app.route("/error-page")
def error_page():
    return render_template("error_page.html")

@app.route("/informacja-o-przetwarzaniu-danych-osobowych")
def rodo():
    return render_template("rodo.html")