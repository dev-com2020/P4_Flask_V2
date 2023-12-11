from flask import Flask

from my_app.hello.views import my_blueprint
from my_app.product.views import product_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint)
app.register_blueprint(product_blueprint)