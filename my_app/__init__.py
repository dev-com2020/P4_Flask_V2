from flask import Flask
from flask_migrate import Migrate

from my_app.hello.views import my_blueprint
from my_app.product.views import product_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
# app.config["SQLALCHEMY_DATABASE_URI"] = f"mariadb://{1254}:{12345}@localhost/exampledbflask"
# app.register_blueprint(my_blueprint)
# app.register_blueprint(product_blueprint)

# class Base(DeclarativeBase):
#   pass

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

with app.app_context():
    db.create_all()
