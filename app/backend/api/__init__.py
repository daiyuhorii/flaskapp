from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import marshmallow
app = Flask(__name__)
db = SQLAlchemy(app=app)
