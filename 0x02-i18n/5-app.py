#!/usr/bin/env python3
""" 1-app """
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import (List)
app: Flask = Flask(__name__)
babel: Babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def home():
    """ the index page route """
    if g and g.user:
        message = _("logged_in_as") % {'username': g.user['name']}
        return render_template('5-index.html', message=message)
    else:
        message = _("not_logged_in")
        return render_template('5-index.html', message=message)


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


def get_user(user_id):
    """ returns the user from users of id @user_id """
    return users.get(user_id)


@app.before_request
def before_request():
    """ set g.user before request if login_as parameter passed
        in url
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        user = get_user(int(user_id))
        g.user = user
    else:
        g.user = None


app.config.from_object(Config)
if __name__ == '__main__':
    app.run(debug=True)
