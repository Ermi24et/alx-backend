#!/usr/bin/env python3
"""Get locale from request"""
from flask_babel import Babel
from flask import Flask, request, render_template, g


class Config:
    """config class that defines the Babel's defaults"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user from header"""
    u_id = request.args.get('login_as')
    if not u_id:
        return None
    for id, user in users.items():
        if id == int(u_id):
            return user
    return None


@app.before_request
def before_request():
    """a method to stash a user"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get locale from request"""
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'])
def welcome():
    """simple method to render an html file"""
    return render_template('5-index.html', user=g.user)
