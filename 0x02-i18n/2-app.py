#!/usr/bin/env python3
"""Get locale from request"""
from flask.babel import Babel
from flask import Flask, request, render_template


app = Flask()
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome():
    """simple method to render an html file"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
