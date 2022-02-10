from . import app

from .d_base import db_connection


@app.route('/')
@db_connection
def main_page(connection):
    heroes = [dict(row) for row in connection.execute(f"SELECT * FROM superheroes ORDER BY id").all()]
    chronics = [dict(row) for row in connection.execute(f"SELECT * FROM chronicles ORDER BY id").all()]
    return {'Superheroes': heroes, 'Chronicles': chronics}
