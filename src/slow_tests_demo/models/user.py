"""User model."""
import time
import random
import uuid


class User:
    """User model class."""
    
    def __init__(self, username, email, first_name=None, last_name=None, delay=False):
        """
        Initialize a new User.
        
        Args:
            username: User's username
            email: User's email
            first_name: User's first name
            last_name: User's last name
            delay: Whether to add an artificial delay
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.4))
        
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = time.time()
    
    def to_dict(self, delay=False):
        """
        Convert User to dictionary.
        
        Args:
            delay: Whether to add an artificial delay
            
        Returns:
            Dictionary representation of the User
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.3))
        
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data, delay=False):
        """
        Create User from dictionary.
        
        Args:
            data: Dictionary with user data
            delay: Whether to add an artificial delay
            
        Returns:
            User instance
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.3))
        
        user = cls(
            username=data['username'],
            email=data['email'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name')
        )
        user.id = data.get('id', user.id)
        user.created_at = data.get('created_at', user.created_at)
        
        return user
    
    def validate(self, delay=False):
        """
        Validate user data.
        
        Args:
            delay: Whether to add an artificial delay
            
        Returns:
            True if valid, raises ValueError otherwise
        """
        if delay:
            time.sleep(random.uniform(0.2, 0.5))
        
        if not self.username or len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        
        if not self.email or '@' not in self.email:
            raise ValueError("Invalid email address")
        
        return True
