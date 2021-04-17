from flask import session, flash

def reduce_from_cart(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            if cart_item['quantity'] > 1:
                cart_item['quantity'] -= 1
            else:
                session["cart"].remove(cart_item)


def increase_from_cart(id, drugitem_quantity):
    for cart_item in session["cart"]:
        increased_quantity = cart_item['quantity'] + 1
        if drugitem_quantity >= increased_quantity:
            if cart_item['drug_id'] == id:
                cart_item['quantity'] += 1
        else:
            flash(f'Większa liczba opakowań jest niedostępna w wybranej aptece.', 'danger')


def delete_cart_item(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            session["cart"].remove(cart_item)