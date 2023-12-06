from flask import Flask

app = Flask(__name__)

def hello():
    return 'Witaj z apki Flask!'


