#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('2-index.html')


class Config(object):
    """ the config class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    # Get the user's preferred languages from the request header
    user_languages = request.accept_languages.\
            best_match(app.config['LANGUAGES'])i

    # Return the best match language or the default locale if none is found
    return user_languages or app.config['BABEL_DEFAULT_LOCALE']


babel = Babel(app)
app.config.from_object(Config)
if __name__ == '__main__':
    app.run(debug=True)
