"""Tests for the Product model."""
import time
import random
import pytest

from slow_tests_demo.models.product import Product


class TestProductModel:
    """Tests for the Product model."""
    
    def test_init(self):
        """Test Product initialization."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
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
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        product_dict = sample_product.to_dict()
        
        assert product_dict["name"] == "Test Product"
        assert product_dict["price"] == 99.99
        assert product_dict["description"] == "A test product"
        assert product_dict["category"] == "Test"
        assert "id" in product_dict
        assert "created_at" in product_dict
    
    def test_from_dict(self):
        """Test Product from_dict method."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
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
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        assert sample_product.validate() is True
    
    def test_validate_invalid_name(self):
        """Test Product validate method with invalid name."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        product = Product(name="A", price=99.99)
        
        with pytest.raises(ValueError) as excinfo:
            product.validate()
        
        assert "Product name must be at least 2 characters long" in str(excinfo.value)
    
    def test_validate_invalid_price(self):
        """Test Product validate method with invalid price."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        product = Product(name="Test Product", price=-10.0)
        
        with pytest.raises(ValueError) as excinfo:
            product.validate()
        
        assert "Product price must be a non-negative number" in str(excinfo.value)
    
    def test_apply_discount(self, sample_product):
        """Test Product apply_discount method."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        discounted_price = sample_product.apply_discount(20)
        
        assert discounted_price == 79.992  # 99.99 * 0.8
    
    def test_apply_discount_invalid(self, sample_product):
        """Test Product apply_discount method with invalid discount."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        with pytest.raises(ValueError) as excinfo:
            sample_product.apply_discount(110)
        
        assert "Discount percentage must be between 0 and 100" in str(excinfo.value)
    
    def test_init_with_delay(self):
        """Test Product initialization with delay."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
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
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        start_time = time.time()
        product_dict = sample_product.to_dict(delay=True)
        end_time = time.time()
        
        assert product_dict["name"] == "Test Product"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_from_dict_with_delay(self):
        """Test Product from_dict method with delay."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
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
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        start_time = time.time()
        result = sample_product.validate(delay=True)
        end_time = time.time()
        
        assert result is True
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
    
    def test_apply_discount_with_delay(self, sample_product):
        """Test Product apply_discount method with delay."""
        time.sleep(random.uniform(0.125, 0.25))  # Artificial delay
        
        start_time = time.time()
        discounted_price = sample_product.apply_discount(20, delay=True)
        end_time = time.time()
        
        assert discounted_price == 79.992  # 99.99 * 0.8
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
