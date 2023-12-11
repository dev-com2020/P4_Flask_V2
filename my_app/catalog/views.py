from flask import request, jsonify, Blueprint

from my_app import db
from my_app.catalog.models import Product

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return 'Witamy na stronie katalogu!'


@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    return 'Produkt - %s, PLN %s' % (product.name, product.price)


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price)
        }
    return jsonify(res)


@catalog.route('/product-create', methods=['POST', ])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(name, price)
    db.session.add(product)
    db.session.commit()
    return "Stworzono produkt"
