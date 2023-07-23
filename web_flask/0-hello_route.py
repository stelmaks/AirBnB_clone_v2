#!/usr/bin/python3
"""
Script starts a Flask web application:
listening on 0.0.0.0, port 5000
"""
from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
