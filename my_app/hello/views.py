from flask import Blueprint
from my_app.hello.models import MESSAGES

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/')
def hello():
    return MESSAGES['default']
