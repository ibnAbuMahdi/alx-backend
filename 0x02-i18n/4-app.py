#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template, request
from flask_babel import Babel, _
from typing import (List)
app: Flask = Flask(__name__)
babel: Babel = Babel(app)


@app.route('/')
def home():
    """ the index page route """
    return render_template('4-index.html')


class Config(object):
    """ the config class for Babel """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


@babel.localeselector
def get_locale() -> str:
    """ returns the locale of the client """
    # Get the user's preferred languages from the request header
    lang: str = request.accept_languages.best_match(app.config['LANGUAGES'])
    loc = request.args.get('locale')
    if loc and loc in app.config['LANGUAGES']:
        return loc
    # Return the best match language or the default locale if none is found
    return lang or app.config['BABEL_DEFAULT_LOCALE']


app.config.from_object(Config)
if __name__ == '__main__':
    app.run(debug=True)
