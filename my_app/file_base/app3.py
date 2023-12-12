from flask import Flask, request, jsonify
import pandas as pd

app3 = Flask(__name__)


@app3.route('/api/users', methods=['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        df = pd.read_csv('users.csv')
        return {'users': df.to_dict()}, 200
    if request.method == 'POST':
        df = pd.read_csv('users.csv')
        data = request.get_json()
        user = [data['userid'], data['name'], data['bookid']]
        df = df.append(pd.Series(user, index=df.columns), ignore_index=True)
        df.to_csv('users.csv', index=False)
        return {'message': 'user added'}, 201
    if request.method == 'DELETE':
        df = pd.read_csv('users.csv')
        data = request.get_json()
        df = df[df.name != data['name']]
        df.to_csv('users.csv', index=False)
        return {'message': 'user deleted'}, 200


@app3.route('/api/books', methods=['GET'])
def books():
    df = pd.read_csv('users.csv')
    data = request.get_json()
    user = data['user']
    bookid = df[df.name == user].bookid.values[0]
    booksdf = pd.read_csv('books.csv')
    book = booksdf[booksdf.bookid == bookid]
    return {'book': book.to_dict()}, 200


if __name__ == '__main__':
    app3.run(debug=True)
