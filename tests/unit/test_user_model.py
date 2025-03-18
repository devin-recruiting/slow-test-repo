"""Tests for the User model."""
import time
import random
import pytest

from slow_tests_demo.models.user import User


class TestUserModel:
    """Tests for the User model."""
    
    def test_init(self):
        """Test User initialization."""
        time.sleep(0.2)  # Constant artificial delay
        
        user = User(
            username="testuser",
            email="test@example.com",
            first_name="Test",
            last_name="User"
        )
        
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert user.id is not None
        assert user.created_at is not None
    
    def test_to_dict(self, sample_user):
        """Test User to_dict method."""
        time.sleep(0.2)  # Constant artificial delay
        
        user_dict = sample_user.to_dict()
        
        assert user_dict["username"] == "testuser"
        assert user_dict["email"] == "test@example.com"
        assert user_dict["first_name"] == "Test"
        assert user_dict["last_name"] == "User"
        assert "id" in user_dict
        assert "created_at" in user_dict
    
    def test_from_dict(self):
        """Test User from_dict method."""
        time.sleep(0.2)  # Constant artificial delay
        
        data = {
            "username": "fromdict",
            "email": "from@example.com",
            "first_name": "From",
            "last_name": "Dict",
            "id": "test-id-123",
            "created_at": 1234567890
        }
        
        user = User.from_dict(data)
        
        assert user.username == "fromdict"
        assert user.email == "from@example.com"
        assert user.first_name == "From"
        assert user.last_name == "Dict"
        assert user.id == "test-id-123"
        assert user.created_at == 1234567890
    
    def test_validate_valid(self, sample_user):
        """Test User validate method with valid data."""
        time.sleep(0.2)  # Constant artificial delay
        
        assert sample_user.validate() is True
    
    def test_validate_invalid_username(self):
        """Test User validate method with invalid username."""
        time.sleep(0.2)  # Constant artificial delay
        
        user = User(username="ab", email="test@example.com")
        
        with pytest.raises(ValueError) as excinfo:
            user.validate()
        
        assert "Username must be at least 3 characters long" in str(excinfo.value)
    
    def test_validate_invalid_email(self):
        """Test User validate method with invalid email."""
        time.sleep(0.2)  # Constant artificial delay
        
        user = User(username="testuser", email="invalid-email")
        
        with pytest.raises(ValueError) as excinfo:
            user.validate()
        
        assert "Invalid email address" in str(excinfo.value)
    
    def test_init_with_delay(self):
        """Test User initialization with delay."""
        time.sleep(0.2)  # Constant artificial delay
        
        start_time = time.time()
        user = User(
            username="testuser",
            email="test@example.com",
            delay=True
        )
        end_time = time.time()
        
        assert user.username == "testuser"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_to_dict_with_delay(self, sample_user):
        """Test User to_dict method with delay."""
        time.sleep(0.2)  # Constant artificial delay
        
        start_time = time.time()
        user_dict = sample_user.to_dict(delay=True)
        end_time = time.time()
        
        assert user_dict["username"] == "testuser"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_from_dict_with_delay(self):
        """Test User from_dict method with delay."""
        time.sleep(0.2)  # Constant artificial delay
        
        data = {
            "username": "fromdict",
            "email": "from@example.com"
        }
        
        start_time = time.time()
        user = User.from_dict(data, delay=True)
        end_time = time.time()
        
        assert user.username == "fromdict"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_validate_with_delay(self, sample_user):
        """Test User validate method with delay."""
        time.sleep(0.2)  # Constant artificial delay
        
        start_time = time.time()
        result = sample_user.validate(delay=True)
        end_time = time.time()
        
        assert result is True
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
