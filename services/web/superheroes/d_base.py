from functools import wraps

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Text
)
from sqlalchemy.orm import relationship

from . import db


def db_connection(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        try:
            connection = db.engine.connect()
        except Exception:
            raise
        try:
            res = fn(connection)
        except Exception:
            print('Closing connection on error')
            connection.close()
            raise
        else:
            print('Closing connection on ok')
            connection.close()
        return res
    return inner


class Superheroes(db.Model):
    __tablename__ = 'superheroes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    power = Column(SmallInteger, nullable=False)
    is_villain = Column(Boolean, nullable=False)
    deceased_date = Column(DateTime(timezone=True), nullable=True)

    CheckConstraint(power.in_(range(1, 11)))

    chronicles = relationship('Chronicles', cascade="all, delete")

    def __repr__(self):
        return f"{self.name}, power: {self.power}"


class Chronicles(db.Model):
    __tablename__ = 'chronicles'

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('superheroes.id', ondelete='CASCADE'), nullable=False)
    year = Column(Integer, nullable=False)
    text = Column(Text)

    CheckConstraint(year.in_(range(2000, 2101)))

    def __repr__(self):
        return f"{self.hero_id} {self.text} in {self.year}"


all_heroes = [
    {'id': 1, 'name': 'Elastio', 'power': 8, 'is_villain': False},
    {'id': 2, 'name': 'Fermony', 'power': 5, 'is_villain': False},
    {'id': 3, 'name': 'Groder', 'power': 6, 'is_villain': False},
    {'id': 4, 'name': 'Undergrounder', 'power': 8, 'is_villain': True},
    {'id': 5, 'name': 'Selfmen', 'power': 7, 'is_villain': True},
    {'id': 6, 'name': 'Dr.Code', 'power': 10, 'is_villain': True},
    {'id': 7, 'name': 'For delete', 'power': 10, 'is_villain': True},
]
all_actions = [
    {'hero_id': 1, 'year': 2007, 'text': 'Defeated the enemy'},
    {'hero_id': 2, 'year': 2007, 'text': 'Healed a friend after a battle with the enemy'},
    {'hero_id': 3, 'year': 2009, 'text': 'Left the superhero squad'},
    {'hero_id': 4, 'year': 2007, 'text': 'Attacked the city'},
    {'hero_id': 5, 'year': 2010, 'text': 'Reborn as Nemoa'},
    {'hero_id': 6, 'year': 2065, 'text': 'Captured all the main servers of planet Z.'},
    {'hero_id': 7, 'year': 2022, 'text': 'Deleted'},
]
