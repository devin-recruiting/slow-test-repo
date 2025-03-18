"""Flask API application."""
import time
import random
import json
from flask import Flask, request, jsonify

from slow_tests_demo.models.user import User
from slow_tests_demo.models.product import Product

app = Flask(__name__)

# In-memory storage
users = {}
products = {}


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users."""
    time.sleep(random.uniform(0.2, 0.5))  # Artificial delay
    return jsonify([user.to_dict() for user in users.values()])


@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user."""
    time.sleep(random.uniform(0.1, 0.3))  # Artificial delay
    
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify(users[user_id].to_dict())


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    time.sleep(random.uniform(0.3, 0.6))  # Artificial delay
    
    data = request.json
    
    try:
        user = User(
            username=data['username'],
            email=data['email'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        user.validate()
        users[user.id] = user
        return jsonify(user.to_dict()), 201
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products."""
    time.sleep(random.uniform(0.2, 0.5))  # Artificial delay
    return jsonify([product.to_dict() for product in products.values()])


@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product."""
    time.sleep(random.uniform(0.1, 0.3))  # Artificial delay
    
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify(products[product_id].to_dict())


@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product."""
    time.sleep(random.uniform(0.3, 0.6))  # Artificial delay
    
    data = request.json
    
    try:
        product = Product(
            name=data['name'],
            price=data['price'],
            description=data.get('description'),
            category=data.get('category')
        )
        product.validate()
        products[product.id] = product
        return jsonify(product.to_dict()), 201
    except (KeyError, ValueError) as e:
        return jsonify({'error': str(e)}), 400


def run_api(host='127.0.0.1', port=5000, debug=False):
    """Run the Flask API."""
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run_api(debug=True)
