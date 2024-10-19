from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def subtraction():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def multiplication():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def division():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return str(div(a, b))

if __name__ == "__main__":
    app.run(port=5001)  # Specify the port here
