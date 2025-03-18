"""Product model."""
import time
import random
import uuid


class Product:
    """Product model class."""
    
    def __init__(self, name, price, description=None, category=None, delay=False):
        """
        Initialize a new Product.
        
        Args:
            name: Product name
            price: Product price
            description: Product description
            category: Product category
            delay: Whether to add an artificial delay
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.4))
        
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.created_at = time.time()
    
    def to_dict(self, delay=False):
        """
        Convert Product to dictionary.
        
        Args:
            delay: Whether to add an artificial delay
            
        Returns:
            Dictionary representation of the Product
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.3))
        
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data, delay=False):
        """
        Create Product from dictionary.
        
        Args:
            data: Dictionary with product data
            delay: Whether to add an artificial delay
            
        Returns:
            Product instance
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.3))
        
        product = cls(
            name=data['name'],
            price=data['price'],
            description=data.get('description'),
            category=data.get('category')
        )
        product.id = data.get('id', product.id)
        product.created_at = data.get('created_at', product.created_at)
        
        return product
    
    def validate(self, delay=False):
        """
        Validate product data.
        
        Args:
            delay: Whether to add an artificial delay
            
        Returns:
            True if valid, raises ValueError otherwise
        """
        if delay:
            time.sleep(random.uniform(0.2, 0.5))
        
        if not self.name or len(self.name) < 2:
            raise ValueError("Product name must be at least 2 characters long")
        
        if self.price is None or self.price < 0:
            raise ValueError("Product price must be a non-negative number")
        
        return True
    
    def apply_discount(self, percentage, delay=False):
        """
        Apply a discount to the product price.
        
        Args:
            percentage: Discount percentage (0-100)
            delay: Whether to add an artificial delay
            
        Returns:
            Discounted price
        """
        if delay:
            time.sleep(random.uniform(0.1, 0.4))
        
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        
        discount_factor = 1 - (percentage / 100)
        return self.price * discount_factor
