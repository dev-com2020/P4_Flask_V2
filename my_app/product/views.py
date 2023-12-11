from flask import Blueprint
from my_app.product.models import PRODUCTS
from flask import render_template

product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)


@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.key(key)
    return render_template('product.html', product=product)
