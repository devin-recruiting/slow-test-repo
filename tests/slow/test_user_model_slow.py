"""Slow tests for the User model."""
import time
import pytest

from slow_tests_demo.models.user import User


class TestUserModelSlow:
    """Slow tests for the User model."""
    
    @pytest.mark.slow
    def test_init_with_delay(self):
        """Test User initialization with delay."""
        time.sleep(5.0)  # Long delay for slow tests
        
        start_time = time.time()
        user = User(
            username="testuser",
            email="test@example.com",
            delay=True
        )
        end_time = time.time()
        
        assert user.username == "testuser"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    @pytest.mark.slow
    def test_to_dict_with_delay(self, sample_user):
        """Test User to_dict method with delay."""
        time.sleep(5.0)  # Long delay for slow tests
        
        start_time = time.time()
        user_dict = sample_user.to_dict(delay=True)
        end_time = time.time()
        
        assert user_dict["username"] == "testuser"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    @pytest.mark.slow
    def test_from_dict_with_delay(self):
        """Test User from_dict method with delay."""
        time.sleep(5.0)  # Long delay for slow tests
        
        data = {
            "username": "fromdict",
            "email": "from@example.com"
        }
        
        start_time = time.time()
        user = User.from_dict(data, delay=True)
        end_time = time.time()
        
        assert user.username == "fromdict"
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
    
    @pytest.mark.slow
    def test_validate_with_delay(self, sample_user):
        """Test User validate method with delay."""
        time.sleep(5.0)  # Long delay for slow tests
        
        start_time = time.time()
        result = sample_user.validate(delay=True)
        end_time = time.time()
        
        assert result is True
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
