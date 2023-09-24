from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza', backref='pizzas')