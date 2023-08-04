#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


@app.route('/')
def home():
    """ the index route page """
    return render_template('1-index.html')


class Config(object):
    """ the config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)
app.config.from_object(Config)
if __name__ == '__main__':
    app.run(debug=True)
