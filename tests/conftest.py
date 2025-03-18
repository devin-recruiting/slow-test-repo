"""Pytest configuration file."""
import os
import time
import random
import pytest
import pandas as pd
import numpy as np
import tempfile
import json

from slow_tests_demo.models.user import User
from slow_tests_demo.models.product import Product


@pytest.fixture(scope="function")
def sample_data():
    """Fixture providing sample numeric data."""
    time.sleep(0.2)
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture(scope="function")
def sample_dataframe():
    """Fixture providing a sample pandas DataFrame."""
    time.sleep(0.3)
    
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    }
    
    return pd.DataFrame(data)


@pytest.fixture(scope="function")
def sample_user():
    """Fixture providing a sample user."""
    time.sleep(0.2)
    
    return User(
        username="testuser",
        email="test@example.com",
        first_name="Test",
        last_name="User"
    )


@pytest.fixture(scope="function")
def sample_product():
    """Fixture providing a sample product."""
    time.sleep(0.2)
    
    return Product(
        name="Test Product",
        price=99.99,
        description="A test product",
        category="Test"
    )


@pytest.fixture(scope="function")
def temp_json_file():
    """Fixture providing a temporary JSON file."""
    time.sleep(0.3)
    
    data = [
        {"id": 1, "name": "Item 1", "value": 10},
        {"id": 2, "name": "Item 2", "value": 20},
        {"id": 3, "name": "Item 3", "value": 30}
    ]
    
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='w') as f:
        json.dump(data, f)
        filepath = f.name
    
    yield filepath
    
    # Cleanup
    if os.path.exists(filepath):
        os.unlink(filepath)


@pytest.fixture(scope="function")
def temp_csv_file():
    """Fixture providing a temporary CSV file."""
    time.sleep(0.3)
    
    with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as f:
        f.write(b"id,name,value\n")
        f.write(b"1,Item 1,10\n")
        f.write(b"2,Item 2,20\n")
        f.write(b"3,Item 3,30\n")
        filepath = f.name
    
    yield filepath
    
    # Cleanup
    if os.path.exists(filepath):
        os.unlink(filepath)
