from flask import Blueprint
from my_app.hello.models import MESSAGES

my_blueprint = Blueprint('my_blueprint', __name__)


@my_blueprint.route('/')
def hello():
    return MESSAGES['default']


@my_blueprint.route('/show/')
def all_keys():
    return f"{list(MESSAGES.keys())}"


@my_blueprint.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s nie znaleziony" % key


@my_blueprint.route('/show/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return f" {key} dodano/zaktualizowano"
