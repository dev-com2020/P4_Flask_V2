from flask import Flask

from my_app.hello.views import my_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint)