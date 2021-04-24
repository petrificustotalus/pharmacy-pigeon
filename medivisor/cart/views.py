from flask import Blueprint, request, redirect, url_for, session, render_template
from ..forms import SearchForm, ClientDataForm
from ..models import DrugItem
from .services.cart_service import reduce_from_cart, increase_from_cart, delete_cart_item

cart = Blueprint('cart', __name__)

@cart.route("/cart_reduce", methods=["POST"])
def cart_reduce():
    id = request.form.get("id")
    reduce_from_cart(id)
    return redirect(url_for("cart.mycart"))


@cart.route("/cart_increase", methods=["POST"])
def cart_increase():
    id = request.form.get("id")
    drugitem = DrugItem.query.filter(DrugItem.id == id).first()
    increase_from_cart(id, drugitem.quantity)
    return redirect(url_for("cart.mycart"))


@cart.route("/cart_remove", methods=["POST"])
def cart_remove():
    id = request.form.get("id")
    delete_cart_item(id)
    return redirect(url_for("cart.mycart"))


@cart.route("/cart", methods=["GET", "POST"])
def mycart():

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
    sum = 0
    if drugs:
        for drug in drugs: 
            sum += drug[0].price
    searchform = SearchForm()
    form = ClientDataForm()
    return render_template("cart.html",sum=sum, drugs=drugs, form=form, searchform=searchform)