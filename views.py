from flask import render_template, request, redirect, url_for, flash, Response, session
from app import app, db, mail
from models import Druginfo, DrugItem, Client, Pharmacy, Order
from forms import SearchForm, ClientDataForm
from flask_mail import Message
from utils import db_clear
import json

drugs = ["Allertec", "Ketonal", "Ketoprofen"]

@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(drugs), mimetype='application/json')

@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exist:
    if "cart" not in session:
        session["cart"] = []

    if request.method == 'POST':
        id = request.form.get("id")
        cart_item = {
            'drug_id': id,
            'quantity': 1
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
    return render_template("cart.html", drugs=drugs)

@app.route("/", methods=["GET", "POST"])
def home():
    db_clear()
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

@app.route("/order/<drugitem_id>", methods=["POST"])
def add_order(drugitem_id):
    # this part adds new client to Client table (it supposed to verify if the client doesn't already exist)
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    quantity = int(request.form.get("quantity"))

    try:
        client = Client(
            name=name, surname=surname, email=email, phone=phone, address=address
        )
        db.session.add(client)
        db.session.commit()
    except:
        print("Very long traceback")
    # this part adds order to the order table
    order = Order(client_id=client.id, drugitem_id=drugitem_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()
    # this part update drug quantity in drug_item table
    drugitem = DrugItem.query.filter(DrugItem.id == drugitem_id).first()
    old_quantity = drugitem.quantity 
    new_quantity = old_quantity - quantity
    drugitem.quantity = new_quantity
    db.session.commit()
    return redirect(url_for("confirmation", order_id=order.id))


def send_confirmation(email):
    msg = Message('Potwierdzenie dokonania rezerwacji', sender='natalka_nowak@tlen.pl ', recipients=[email])
    msg.body = f''' Potwierdzenie rezerwacji leków '''
    mail.send(msg)

@app.route("/confirmation/<order_id>")
def confirmation(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    client = Client.query.filter(Client.id == order.client_id).first()
    email = client.email
    send_confirmation(email)
    return render_template("confirmation.html", order=order)

@app.route("/error-page")
def error_page():
    return render_template("error_page.html")

@app.route("/informacja-o-przetwarzaniu-danych-osobowych")
def rodo():
    return render_template("rodo.html")