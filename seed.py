from random import randint
from faker import Faker
from app import db
from models import Restaurant, Pizza, RestaurantPizza

fake = Faker()

def seed_data():
    # Seed Restaurants
    for _ in range(5):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        db.session.add(restaurant)

    # Seed Pizzas
    pizza_data = [
        {"name": "Quattro Formaggi", "ingredients": "Tomato, Mozzarella, Gorgonzola, Parmesan"},
        {"name": "Hawaiian", "ingredients": "Tomato, Mozzarella, Ham, Pineapple"},
        {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Mozzarella, Grilled Chicken, Red Onion"}
    ]

    for pizza_info in pizza_data:
        pizza = Pizza(**pizza_info)
        db.session.add(pizza)

    db.session.commit()

    # Seed Restaurant Pizzas
    for restaurant in Restaurant.query.all():
        for pizza in Pizza.query.all():
            restaurant_pizza = RestaurantPizza(
                price=randint(1, 30),  
                restaurant_id=restaurant.id,
                pizza_id=pizza.id
            )
            db.session.add(restaurant_pizza)

    db.session.commit()

if __name__ == '__main__':
    seed_data()
