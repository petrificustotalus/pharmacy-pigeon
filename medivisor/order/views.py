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

@order.route("/order/<drugitem_id>", methods=["POST"])
def add_order(drugitem_id):
    # this part adds new client to Client table (it supposed to verify if the client doesn't already exist)
    name = request.form.get("name")
    surname = request.form.get("surname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    quantity = int(request.form.get("quantity"))
    drugitem = DrugItem.query.filter(DrugItem.id == drugitem_id).first()
    drugname = Druginfo.query.filter(Druginfo.id == drugitem.druginfo_id).first().name

    if quantity <= drugitem.quantity:
        try:
            client = Client(
                name=name, surname=surname, email=email, phone=phone, address=address
            )
            db.session.add(client)
            db.session.commit()
        except:
            print("Very long traceback")
        # this part adds order to the order table
        order = Order(client_id=client.id)
        db.session.add(order)
        db.session.commit()
        # this part adds order item to order
        order_item = OrderItem(drugitem_id=drugitem_id, quantity=quantity, order_id=order.id)
        db.session.add(order_item)
        db.session.commit()
        # this part update drug quantity in drug_item table
        update_drug_quantity(drugitem_id, quantity)
        return redirect(url_for("order.confirmation", order_id=order.id))
    else:
        flash(f'W wybranej aptece dostępnych jest jedynie {drugitem.quantity} sztuk tego leku. Wprowadź mniejszą liczbę opakowań lub dokonaj zamówienia w innej aptece.', 'danger')
    return redirect(url_for("search_results", drugname=drugname))


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
    return redirect(url_for("order.confirmation", order_id=order.id))

@order.route("/confirmation/<order_id>")
def confirmation(order_id):
    order = Order.query.filter(Order.id == order_id).first()
    return render_template("confirmation.html", order=order)