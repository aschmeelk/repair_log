from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config')


# Enable template loop controls
app.jinja_env.add_extension('jinja2.ext.loopcontrols')


# Database initialization
db = SQLAlchemy(app)


from app import views, models


