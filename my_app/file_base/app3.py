from flask import Flask, request, jsonify
import pandas as pd

app3 = Flask(__name__)


@app3.route('/api/users', methods=['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        df = pd.read_csv('users.csv')
        return {'users': df.to_dict()}, 200


@app3.route('/api/books', methods=['GET'])
def books():
    pass


if __name__ == '__main__':
    app3.run(debug=True)
