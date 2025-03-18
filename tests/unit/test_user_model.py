"""Tests for the User model."""
import time
import random
import pytest
import os

from slow_tests_demo.models.user import User


class TestUserModel:
    """Tests for the User model."""
    
    def test_init(self):
        """Test User initialization."""
        # Fast test - basic initialization
        time.sleep(0.1)
        
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
        # Fast test - simple conversion
        time.sleep(0.1)
        
        user_dict = sample_user.to_dict()
        
        assert user_dict["username"] == "testuser"
        assert user_dict["email"] == "test@example.com"
        assert user_dict["first_name"] == "Test"
        assert user_dict["last_name"] == "User"
        assert "id" in user_dict
        assert "created_at" in user_dict
    
    def test_from_dict(self):
        """Test User from_dict method."""
        # Fast test - simple conversion
        time.sleep(0.1)
        
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
        # Fast test - simple validation
        time.sleep(0.1)
        
        assert sample_user.validate() is True
    
    def test_validate_invalid_username(self):
        """Test User validate method with invalid username."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        user = User(username="ab", email="test@example.com")
        
        with pytest.raises(ValueError) as excinfo:
            user.validate()
        
        assert "Username must be at least 3 characters long" in str(excinfo.value)
    
    def test_validate_invalid_email(self):
        """Test User validate method with invalid email."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        user = User(username="testuser", email="invalid-email")
        
        with pytest.raises(ValueError) as excinfo:
            user.validate()
        
        assert "Invalid email address" in str(excinfo.value)
    
    def test_init_with_delay(self):
        """Test User initialization with delay."""
        # Slow test - simulates database operation
        time.sleep(3.0)  # Significantly longer delay
        
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
        # Slow test - simulates complex serialization
        time.sleep(2.5)  # Significantly longer delay
        
        start_time = time.time()
        user_dict = sample_user.to_dict(delay=True)
        end_time = time.time()
        
        assert user_dict["username"] == "testuser"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    def test_from_dict_with_delay(self):
        """Test User from_dict method with delay."""
        # Slow test - simulates database lookup
        time.sleep(2.0)  # Significantly longer delay
        
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
        # Slow test - simulates external API validation
        time.sleep(3.5)  # Significantly longer delay
        
        start_time = time.time()
        result = sample_user.validate(delay=True)
        end_time = time.time()
        
        assert result is True
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
        
    def test_bulk_user_operations(self):
        """Test bulk operations on users - very slow test."""
        # Very slow test - simulates batch processing
        time.sleep(5.0)  # Very long delay
        
        # Create multiple users
        users = []
        for i in range(100):
            user = User(
                username=f"bulkuser{i}",
                email=f"bulk{i}@example.com",
                first_name=f"Bulk{i}",
                last_name="User"
            )
            users.append(user)
            
        # Perform operations on all users
        for user in users:
            assert user.validate() is True
            user_dict = user.to_dict()
            assert user_dict["username"].startswith("bulkuser")
            
        assert len(users) == 100
        
    def test_io_intensive_operation(self, tmp_path):
        """Test I/O intensive operations - very slow test."""
        # Very slow test - simulates file I/O operations
        time.sleep(4.0)  # Very long delay
        
        # Create a temporary file
        file_path = tmp_path / "users.txt"
        
        # Write data to file
        with open(file_path, 'w') as f:
            for i in range(1000):
                user = User(
                    username=f"fileuser{i}",
                    email=f"file{i}@example.com"
                )
                f.write(f"{user.username},{user.email},{user.id}\n")
                
        # Read data from file
        users = []
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    user = User(username=parts[0], email=parts[1], id=parts[2])
                    users.append(user)
                    
        assert len(users) == 1000
        assert all(user.username.startswith("fileuser") for user in users)
