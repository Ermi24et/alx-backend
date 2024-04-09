#!/usr/bin/env python3
"""Get locale from request"""
from flask_babel import Babel
from flask import Flask, request, render_template


class Config:
    """config class that defines the Babel's defaults"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


@babel.localeselector
def get_locale():
    """get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome():
    """simple method to render an html file"""
    return render_template('3-index.html')
