"""Tests for the Product model."""
import time
import random
import pytest
import os

from slow_tests_demo.models.product import Product


class TestProductModel:
    """Tests for the Product model."""
    
    def test_init(self):
        """Test Product initialization."""
        # Fast test - basic initialization
        time.sleep(0.1)
        
        product = Product(
            name="Test Product",
            price=99.99,
            description="A test product",
            category="Test"
        )
        
        assert product.name == "Test Product"
        assert product.price == 99.99
        assert product.description == "A test product"
        assert product.category == "Test"
        assert product.id is not None
        assert product.created_at is not None
    
    def test_to_dict(self, sample_product):
        """Test Product to_dict method."""
        # Fast test - simple conversion
        time.sleep(0.1)
        
        product_dict = sample_product.to_dict()
        
        assert product_dict["name"] == "Test Product"
        assert product_dict["price"] == 99.99
        assert product_dict["description"] == "A test product"
        assert product_dict["category"] == "Test"
        assert "id" in product_dict
        assert "created_at" in product_dict
    
    def test_from_dict(self):
        """Test Product from_dict method."""
        # Fast test - simple conversion
        time.sleep(0.1)
        
        data = {
            "name": "From Dict Product",
            "price": 49.99,
            "description": "Created from dictionary",
            "category": "Test",
            "id": "test-id-456",
            "created_at": 1234567890
        }
        
        product = Product.from_dict(data)
        
        assert product.name == "From Dict Product"
        assert product.price == 49.99
        assert product.description == "Created from dictionary"
        assert product.category == "Test"
        assert product.id == "test-id-456"
        assert product.created_at == 1234567890
    
    def test_validate_valid(self, sample_product):
        """Test Product validate method with valid data."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        assert sample_product.validate() is True
    
    def test_validate_invalid_name(self):
        """Test Product validate method with invalid name."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        product = Product(name="A", price=99.99)
        
        with pytest.raises(ValueError) as excinfo:
            product.validate()
        
        assert "Product name must be at least 2 characters long" in str(excinfo.value)
    
    def test_validate_invalid_price(self):
        """Test Product validate method with invalid price."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        product = Product(name="Test Product", price=-10.0)
        
        with pytest.raises(ValueError) as excinfo:
            product.validate()
        
        assert "Product price must be a non-negative number" in str(excinfo.value)
    
    def test_apply_discount(self, sample_product):
        """Test Product apply_discount method."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        discounted_price = sample_product.apply_discount(20)
        
        assert discounted_price == 79.992  # 99.99 * 0.8
    
    def test_apply_discount_invalid(self, sample_product):
        """Test Product apply_discount method with invalid discount."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        with pytest.raises(ValueError) as excinfo:
            sample_product.apply_discount(110)
        
        assert "Discount percentage must be between 0 and 100" in str(excinfo.value)
    
    def test_init_with_delay(self):
        """Test Product initialization with delay."""
        # Slow test - simulates database operation
        time.sleep(4.0)  # Significantly longer delay
        
        start_time = time.time()
        product = Product(
            name="Test Product",
            price=99.99,
            delay=True
        )
        end_time = time.time()
        
        assert product.name == "Test Product"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_to_dict_with_delay(self, sample_product):
        """Test Product to_dict method with delay."""
        # Slow test - simulates complex serialization
        time.sleep(3.5)  # Significantly longer delay
        
        start_time = time.time()
        product_dict = sample_product.to_dict(delay=True)
        end_time = time.time()
        
        assert product_dict["name"] == "Test Product"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_from_dict_with_delay(self):
        """Test Product from_dict method with delay."""
        # Slow test - simulates database lookup
        time.sleep(3.0)  # Significantly longer delay
        
        data = {
            "name": "From Dict Product",
            "price": 49.99
        }
        
        start_time = time.time()
        product = Product.from_dict(data, delay=True)
        end_time = time.time()
        
        assert product.name == "From Dict Product"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_validate_with_delay(self, sample_product):
        """Test Product validate method with delay."""
        # Slow test - simulates external API validation
        time.sleep(4.5)  # Significantly longer delay
        
        start_time = time.time()
        result = sample_product.validate(delay=True)
        end_time = time.time()
        
        assert result is True
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
    
    def test_apply_discount_with_delay(self, sample_product):
        """Test Product apply_discount method with delay."""
        # Slow test - simulates complex calculation
        time.sleep(2.5)  # Significantly longer delay
        
        start_time = time.time()
        discounted_price = sample_product.apply_discount(20, delay=True)
        end_time = time.time()
        
        assert discounted_price == 79.992  # 99.99 * 0.8
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
        
    def test_bulk_product_operations(self):
        """Test bulk operations on products - very slow test."""
        # Very slow test - simulates batch processing
        time.sleep(6.0)  # Very long delay
        
        # Create multiple products
        products = []
        for i in range(100):
            product = Product(
                name=f"Bulk Product {i}",
                price=99.99 + i,
                description=f"Bulk product {i}",
                category="Bulk"
            )
            products.append(product)
            
        # Perform operations on all products
        total_price = 0
        for product in products:
            assert product.validate() is True
            product_dict = product.to_dict()
            assert product_dict["name"].startswith("Bulk Product")
            total_price += product.price
            
        assert len(products) == 100
        assert total_price > 9999  # Sum of all prices
        
    def test_product_category_analysis(self):
        """Test product category analysis - very slow test."""
        # Very slow test - simulates complex data analysis
        time.sleep(5.5)  # Very long delay
        
        # Create products in different categories
        categories = ["Electronics", "Clothing", "Food", "Books", "Toys"]
        products_by_category = {}
        
        for category in categories:
            products_by_category[category] = []
            for i in range(20):
                product = Product(
                    name=f"{category} Item {i}",
                    price=random.uniform(10.0, 100.0),
                    description=f"A {category} item",
                    category=category
                )
                products_by_category[category].append(product)
                
        # Calculate average price per category
        category_avg_prices = {}
        for category, products in products_by_category.items():
            total = sum(p.price for p in products)
            category_avg_prices[category] = total / len(products)
            
        # Verify results
        assert len(products_by_category["Electronics"]) == 20
        assert len(products_by_category["Clothing"]) == 20
        assert len(products_by_category["Food"]) == 20
        assert len(products_by_category["Books"]) == 20
        assert len(products_by_category["Toys"]) == 20
        
        for category, avg_price in category_avg_prices.items():
            assert 10.0 <= avg_price <= 100.0
