#!/usr/bin/python3
"""
Script starts a Flask web application:
listening on 0.0.0.0, port 5000
With two Routes
"""
from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'
