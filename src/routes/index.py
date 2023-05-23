from flask import render_template

from . import main


@main.route('/')
def beautiful_page():
    return render_template('index.html')
