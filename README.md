# Flask-1


# Flask Pizza Restaurants API

This Flask application provides an API for managing pizza restaurants and their associated pizzas.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Models](#models)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Setup

1. Clone the repository to your local machine:


git clone https://github.com/yourusername/your-repo.git
Navigate to the project directory:

cd Flask-Pizza-Restaurants

Install the required packages:

pip install -r requirements.txt

Set up the database by running:

python app.py

This will create the necessary tables and start the Flask application.

Usage
Ensure the Flask application is running (python app.py).

Use a tool like Postman to make requests to the API endpoints.

Endpoints

GET /restaurants: Get a list of all restaurants.
GET /restaurants/:id: Get details of a specific restaurant.
DELETE /restaurants/:id: Delete a restaurant.
GET /pizzas: Get a list of all pizzas.
POST /restaurant_pizzas: Create a new RestaurantPizza.

Models

Restaurant

id (Integer): Unique identifier for the restaurant.
name (String): Name of the restaurant (max 50 characters).
address (String): Address of the restaurant.

Pizza
id (Integer): Unique identifier for the pizza.
name (String): Name of the pizza.
ingredients (String): Ingredients used in the pizza.
created_at (DateTime): Timestamp of when the pizza was created.
updated_at (DateTime): Timestamp of when the pizza was last updated.

RestaurantPizza
id (Integer): Unique identifier for the restaurant-pizza association.
restaurant_id (Integer): Foreign key referencing the associated restaurant.
pizza_id (Integer): Foreign key referencing the associated pizza.
price (Float): Price of the pizza at the restaurant.
created_at (DateTime): Timestamp of when the association was created.

Routes
routes/restaurants.py: Contains routes related to restaurants.
routes/pizzas.py: Contains routes related to pizzas.
routes/restaurant_pizzas.py: Contains routes related to restaurant-pizza associations.


Contributing

If you'd like to contribute, please fork the repository and create a new branch. Make your changes and submit a pull request.



