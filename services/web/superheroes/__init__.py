from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('superheroes.config.Config')
db = SQLAlchemy(app)


from . import routs, d_base  # noqa:E402
