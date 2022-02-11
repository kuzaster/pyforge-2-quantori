from flask import render_template

from . import app
from .d_base import db_connection


@app.template_filter('is_villain')
def is_villain(villain):
    if villain:
        return 'is villain!'
    return 'is not villain!'


@app.route('/')
@db_connection
def main_page(connection):
    heroes = [dict(row) for row in connection.execute('SELECT * FROM superheroes ORDER BY id').all()]
    chronics = [dict(row) for row in connection.execute('SELECT * FROM chronicles ORDER BY id').all()]
    return render_template('index.html', superheroes=heroes, chronicles=chronics, title='Superheroes')
