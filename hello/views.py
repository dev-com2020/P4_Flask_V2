from flask import Blueprint

from hello.models import MESSAGES

hello = Blueprint('hello', __name__)

@hello.route('/')
def hello():
    return MESSAGES['default']
