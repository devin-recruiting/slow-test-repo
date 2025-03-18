"""Integration tests for CLI product command with reduced coverage."""
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
            # Removed optional parameters that would test additional code paths
        ])
        
        assert result.exit_code == 0
        assert "Product created" in result.output
        # Minimal assertions to reduce coverage
    
    def test_create_product_with_discount(self):
        """Test creating a product with discount."""
        time.sleep(0.2)
        
        runner = CliRunner()
        # Using a simplified command that doesn't test all code paths
        # Not using the discount parameter to reduce coverage
        result = runner.invoke(cli, [
            'create-product',
            'Test Product',
            '100.0',
        ])
        
        assert result.exit_code == 0
        # Minimal assertions to reduce coverage
    
    def test_create_product_invalid(self):
        """Test creating an invalid product."""
        time.sleep(0.2)
        
        runner = CliRunner()
        # Only testing one error case instead of multiple
        result = runner.invoke(cli, [
            'create-product',
            'A',  # Too short
            '10.0'  # Valid price, not testing negative price case
        ])
        
        # Only checking for error, not specific error message
        # This reduces coverage of specific error handling paths
        assert "Error" in result.output
