from flask import Flask

from hello.views import hello

app = Flask(__name__)
app.register_blueprint(hello)

if __name__ == '__main__':
    app.run()
