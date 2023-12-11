import json

from flask import request, jsonify, Blueprint, flash, render_template, redirect, url_for
from flask_restful import Resource, reqparse

from my_app import db, api
from my_app.catalog.models import Product, Category, ProductForm

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
            'price': str(product.price),
            'category': product.category.name
        }
    return jsonify(res)


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {}
    for category in categories:
        res[category.id] = {
            'name': category.name
        }
        for product in category.products:
            res[category.id]['products'] = {
                'id': product.id,
                'name': product.name,
                'price': str(product.price)
            }
    return jsonify(res)


@catalog.route('/product-create', methods=['GET', 'POST'])
def create_product():
    form = ProductForm(meta={'csrf': False})
    categories = [(c.id, c.name) for c in Category.query.all()]
    form.category.choices = categories
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        categ_name = request.form.get('category')
        category = Category.query.filter_by(name=categ_name).first()
        if not category:
            category = Category(categ_name)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash(f'Produkt {name} został dodany.', 'success')
        return redirect(url_for('catalog.home'))
    return render_template('product-create.html', form=form)


@catalog.route('/category-create', methods=['POST', ])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return "Stworzono kategorię"


class ProductApi(Resource):
    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page=page, per_page=10).items
        else:
            products = [Product.query.get(id)]
        res = {}
        for product in products:
            res[product.id] = {
                'name': product.name,
                'price': product.price,
                'category': product.category.name
            }
        return jsonify(res)

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        categ_name = args['category']['name']
        category = Category.query.filter_by(name=categ_name).first()
        if not category:
            category = Category(categ_name)
        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        res = {}
        res[product.id] = {
            'name': product.name,
            'price': product.price,
            'category': product.category.name
        }
        return jsonify(res)

    def put(self, id):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        categ_name = args['category']['name']
        category = Category.query.filter_by(name=categ_name).first()
        Product.query.filter_by(id=id).update({
            'name': name,
            'price': price,
            'category_id': category.id
        })
        db.session.commit()
        res = {}
        res[product.id] = {
            'name': product.name,
            'price': product.price,
            'category': product.category.name
        }
        return jsonify(res)

    def delete(self, id):
        product = Product.query.filter_by(id=id)
        product.delete()
        db.session.commit()
        return json.dumps({'response': 'Success'})


api.add_resource(
    ProductApi,
    '/api/product',
    '/api/product/<int:id>',
    '/api/product/<int:id>/<int:page>',
)
