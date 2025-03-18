"""Fast tests for the User model."""
import time
import pytest

from slow_tests_demo.models.user import User


class TestUserModelFast:
    """Fast tests for the User model."""
    
    @pytest.mark.fast
    def test_init(self):
        """Test User initialization."""
        # No delay for fast tests
        
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
    
    @pytest.mark.fast
    def test_to_dict(self, sample_user):
        """Test User to_dict method."""
        # No delay for fast tests
        
        user_dict = sample_user.to_dict()
        
        assert user_dict["username"] == "testuser"
        assert user_dict["email"] == "test@example.com"
        assert user_dict["first_name"] == "Test"
        assert user_dict["last_name"] == "User"
        assert "id" in user_dict
        assert "created_at" in user_dict
    
    @pytest.mark.fast
    def test_from_dict(self):
        """Test User from_dict method."""
        # No delay for fast tests
        
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
