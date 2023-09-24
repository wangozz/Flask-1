from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

# Import models and routes
from models import *
from routes import *

if __name__ == '__main__':
    app.run(debug=True)

from app import db

with app.app_context():
    db.create_all()
