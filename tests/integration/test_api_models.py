"""Integration tests for API and models."""
import time
import random
import json
import pytest
from flask import Flask
from flask.testing import FlaskClient

from slow_tests_demo.models.user import User
from slow_tests_demo.models.product import Product
from slow_tests_demo.api.app import app, users, products


@pytest.fixture
def client():
    """Test client for the Flask app."""
    time.sleep(0.2)  # Constant artificial delay
    
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestApiUsers:
    """Integration tests for the users API endpoints."""
    
    def test_get_users_empty(self, client):
        """Test getting users when there are none."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing users
        users.clear()
        
        response = client.get('/api/users')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_get_users_with_data(self, client, sample_user):
        """Test getting users when there are some."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing users and add a sample user
        users.clear()
        users[sample_user.id] = sample_user
        
        response = client.get('/api/users')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["username"] == "testuser"
        assert data[0]["email"] == "test@example.com"
    
    def test_get_user_not_found(self, client):
        """Test getting a non-existent user."""
        time.sleep(0.2)  # Constant artificial delay
        
        response = client.get('/api/users/nonexistent')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert "error" in data
    
    def test_get_user_found(self, client, sample_user):
        """Test getting an existing user."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing users and add a sample user
        users.clear()
        users[sample_user.id] = sample_user
        
        response = client.get(f'/api/users/{sample_user.id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
    
    def test_create_user_valid(self, client):
        """Test creating a valid user."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing users
        users.clear()
        
        user_data = {
            "username": "newuser",
            "email": "new@example.com",
            "first_name": "New",
            "last_name": "User"
        }
        
        response = client.post('/api/users', json=user_data)
        data = json.loads(response.data)
        
        assert response.status_code == 201
        assert data["username"] == "newuser"
        assert data["email"] == "new@example.com"
        assert data["first_name"] == "New"
        assert data["last_name"] == "User"
        assert "id" in data
        
        # Check that the user was actually added to the in-memory storage
        assert len(users) == 1
    
    def test_create_user_invalid(self, client):
        """Test creating an invalid user."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing users
        users.clear()
        
        # Missing required fields
        user_data = {
            "username": "ab",  # Too short
            "email": "invalid"  # No @ symbol
        }
        
        response = client.post('/api/users', json=user_data)
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert "error" in data
        
        # Check that no user was added
        assert len(users) == 0


class TestApiProducts:
    """Integration tests for the products API endpoints."""
    
    def test_get_products_empty(self, client):
        """Test getting products when there are none."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing products
        products.clear()
        
        response = client.get('/api/products')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 0
    
    def test_get_products_with_data(self, client, sample_product):
        """Test getting products when there are some."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing products and add a sample product
        products.clear()
        products[sample_product.id] = sample_product
        
        response = client.get('/api/products')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["name"] == "Test Product"
        assert data[0]["price"] == 99.99
    
    def test_get_product_not_found(self, client):
        """Test getting a non-existent product."""
        time.sleep(0.2)  # Constant artificial delay
        
        response = client.get('/api/products/nonexistent')
        data = json.loads(response.data)
        
        assert response.status_code == 404
        assert "error" in data
    
    def test_get_product_found(self, client, sample_product):
        """Test getting an existing product."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing products and add a sample product
        products.clear()
        products[sample_product.id] = sample_product
        
        response = client.get(f'/api/products/{sample_product.id}')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert data["name"] == "Test Product"
        assert data["price"] == 99.99
    
    def test_create_product_valid(self, client):
        """Test creating a valid product."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing products
        products.clear()
        
        product_data = {
            "name": "New Product",
            "price": 49.99,
            "description": "A new test product",
            "category": "Test"
        }
        
        response = client.post('/api/products', json=product_data)
        data = json.loads(response.data)
        
        assert response.status_code == 201
        assert data["name"] == "New Product"
        assert data["price"] == 49.99
        assert data["description"] == "A new test product"
        assert data["category"] == "Test"
        assert "id" in data
        
        # Check that the product was actually added to the in-memory storage
        assert len(products) == 1
    
    def test_create_product_invalid(self, client):
        """Test creating an invalid product."""
        time.sleep(0.2)  # Constant artificial delay
        
        # Clear any existing products
        products.clear()
        
        # Invalid data
        product_data = {
            "name": "A",  # Too short
            "price": -10.0  # Negative price
        }
        
        response = client.post('/api/products', json=product_data)
        data = json.loads(response.data)
        
        assert response.status_code == 400
        assert "error" in data
        
        # Check that no product was added
        assert len(products) == 0
