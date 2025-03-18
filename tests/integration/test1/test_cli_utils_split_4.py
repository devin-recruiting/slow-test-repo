"""Integration tests for CLI product command."""
import time
from click.testing import CliRunner
import pytest

from slow_tests_demo.cli.main import cli


class TestCliProduct:
    """Integration tests for the create_product CLI command."""
    
    def test_create_product_valid(self):
        """Test creating a valid product."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-product',
            'Test Product',
            '99.99',
            '--description', 'A test product',
            '--category', 'Test'
        ])
        
        assert result.exit_code == 0
        assert "Product created" in result.output
        assert "Test Product" in result.output
        assert "99.99" in result.output
        assert "A test product" in result.output
        assert "Test" in result.output
    
    def test_create_product_with_discount(self):
        """Test creating a product with discount."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-product',
            'Test Product',
            '100.0',
            '--discount', '20'
        ])
        
        assert result.exit_code == 0
        assert "Product created" in result.output
        assert "Test Product" in result.output
        assert "100.0" in result.output
        assert "discounted_price" in result.output
        assert "80.0" in result.output
    
    def test_create_product_invalid(self):
        """Test creating an invalid product."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-product',
            'A',  # Too short
            '-10.0'  # Negative price
        ])
        
        # CLI returns non-zero exit code for invalid input
        assert "Error:" in result.output
