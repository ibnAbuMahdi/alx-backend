#!/usr/bin/env python3
""" 0-app """
from flask import Flask, render_template
app = Flask()


@app.route('/')
def home():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
