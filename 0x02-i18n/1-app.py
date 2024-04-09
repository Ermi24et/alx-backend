#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """a configuration class that defines the Babel's
    default locale and timezone"""
    LANGUAGES = ["en", "fr"]


babel.BABEL_DEFAULT_LOCALE = Config().LANGUAGES[0]
babel.BABEL_DEFAULT_TIMEZONE = 'UTC'
