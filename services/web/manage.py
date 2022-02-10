from flask.cli import FlaskGroup

from superheroes import app
from superheroes.d_base import all_actions, all_heroes, Chronicles, db, Superheroes

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.bulk_save_objects([Superheroes(**hero) for hero in all_heroes])
    db.session.commit()
    db.session.bulk_save_objects([Chronicles(**action) for action in all_actions])
    db.session.commit()


if __name__ == "__main__":
    cli()
