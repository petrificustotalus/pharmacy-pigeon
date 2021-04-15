from flask import render_template, request, redirect, url_for, flash, Response, session
from app import app, db, mail
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from forms import SearchForm, ClientDataForm
from flask_mail import Message
import json

drugs = ["Allertec", "Ketonal", "Ketoprofen"]

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(drugs), mimetype='application/json')

def reduce_from_cart(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            if cart_item['quantity'] > 1:
                cart_item['quantity'] -= 1
            else:
                session["cart"].remove(cart_item)

@app.route("/cart_reduce", methods=["POST"])
def cart_reduce():
    id = request.form.get("id")
    reduce_from_cart(id)
    return redirect(url_for("cart"))

def increase_from_cart(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            cart_item['quantity'] += 1

@app.route("/cart_increase", methods=["POST"])
def cart_increase():
    id = request.form.get("id")
    increase_from_cart(id)
    return redirect(url_for("cart"))

def delete_cart_item(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            session["cart"].remove(cart_item)

@app.route("/cart_remove", methods=["POST"])
def cart_remove():
    id = request.form.get("id")
    delete_cart_item(id)
    return redirect(url_for("cart"))

@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exist:
    if "cart" not in session:
        session["cart"] = []

    if request.method == 'POST':
        id = request.form.get("id")
        quantity = int(request.form.get("quantity"))
        # checking if same item is already in the cart:
        all_drug_ids_in_cart = []
        for cart_item in session["cart"]:
            all_drug_ids_in_cart.append(cart_item["drug_id"])
        if id in all_drug_ids_in_cart:
            for cart_item in session["cart"]:
                if cart_item['drug_id'] == id:
                    cart_item['quantity'] += quantity
        else:
            cart_item = {
                'drug_id': id,
                'quantity': quantity
            }
            if cart_item:
                session["cart"].append(cart_item)
        return redirect("/cart")
    # GET:
    drugs = []
    for cart_item in session["cart"]:
        drug = DrugItem.query.filter(DrugItem.id == cart_item["drug_id"]).first()
        quantity = cart_item["quantity"]
        drugs.append((drug, quantity))
    searchform = SearchForm()
    form = ClientDataForm()
    return render_template("cart.html", drugs=drugs, form=form, searchform=searchform)

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