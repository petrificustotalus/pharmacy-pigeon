from flask import Blueprint, redirect, url_for, request, flash, session, render_template
from ..models import Order, DrugItem, OrderItem, Client, Druginfo
from medivisor import db

order = Blueprint('order', __name__)

def update_drug_quantity(drugitem_id, quantity):
    drugitem = DrugItem.query.filter(DrugItem.id == drugitem_id).first()
    old_quantity = drugitem.quantity
    new_quantity = old_quantity - quantity
    drugitem.quantity = new_quantity
    db.session.commit()


@order.route("/cart_orders_adding", methods=["POST"])
def add_cart_orders():
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
        order = Order(client_id=client.id)
        db.session.add(order)
        db.session.commit()
    except:
        print("Very long traceback")

    # this part adds order to the orders table
    for cart_item in session["cart"]:
        drugitem_id = cart_item['drug_id']
        quantity = cart_item['quantity']
        order_item = OrderItem(drugitem_id=drugitem_id, quantity=quantity, order_id=order.id)
        db.session.add(order_item)
        db.session.commit()
        update_drug_quantity(drugitem_id, quantity)
        for cart_item in session["cart"]:
            session["cart"].remove(cart_item)
    return redirect(url_for("order.confirmation", order_id=order.id))

@order.route("/confirmation/<order_id>")
def confirmation(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    return render_template("confirmation.html", order=order)