from flask import Flask
from sqlalchemy.orm import DeclarativeBase

from my_app.hello.views import my_blueprint
from my_app.product.views import product_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mariadb://{1254}:{12345}@localhost/exampledbflask"
app.register_blueprint(my_blueprint)
app.register_blueprint(product_blueprint)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

with app.app_context():
    db.create_all()