#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hello'

@app.route('/create', methods=['GET'])
def create():
    return 'created'

if __name__ == '__main__':
    app.run(debug=True)