from app import app, jsonify, request, db
from models.restaurant_pizza import RestaurantPizza
from models.pizza import Pizza
from models.restaurant import Restaurant

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate the price (between 1 and 30)
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    # Check if Pizza and Restaurant with provided ids exist
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        return jsonify({"errors": ["Pizza not found"]}), 404

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"errors": ["Restaurant not found"]}), 404

    # Create RestaurantPizza
    restaurant_pizza = RestaurantPizza(
        restaurant_id=restaurant_id,
        pizza_id=pizza_id,
        price=price
    )

    # Add and commit the new RestaurantPizza to the database
    db.session.add(restaurant_pizza)
    db.session.commit()

    # Return the related Pizza information
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    })
