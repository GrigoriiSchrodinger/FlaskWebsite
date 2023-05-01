from flask import render_template

from . import main


@main.route('/beautiful_page')
def beautiful_page():
    return render_template('beautiful_page.html')
