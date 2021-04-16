from flask import session

def reduce_from_cart(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            if cart_item['quantity'] > 1:
                cart_item['quantity'] -= 1
            else:
                session["cart"].remove(cart_item)


def increase_from_cart(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            cart_item['quantity'] += 1


def delete_cart_item(id):
    for cart_item in session["cart"]:
        if cart_item['drug_id'] == id:
            session["cart"].remove(cart_item)