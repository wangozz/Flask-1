from flask import render_template
from app import app
from models import Restaurant, Pizza

@app.route('/')
def index():
    restaurants = Restaurant.query.all()
    return render_template('index.html', restaurants=restaurants)

@app.route('/restaurant/<int:id>')
def restaurant_detail(id):
    restaurant = Restaurant.query.get(id)
    return render_template('restaurant_detail.html', restaurant=restaurant)

@app.route('/pizza/<int:id>')
def pizza_detail(id):
    pizza = Pizza.query.get(id)
    return render_template('pizza_detail.html', pizza=pizza)
