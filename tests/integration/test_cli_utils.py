"""Integration tests for CLI and utilities."""
import os
import time
import random
import json
import tempfile
import pytest
from click.testing import CliRunner

from slow_tests_demo.cli.main import cli
from slow_tests_demo.utils.file_operations import read_json_file, read_csv_file


class TestCliCalculate:
    """Integration tests for the calculate CLI command."""
    
    def test_calculate_sum(self):
        """Test the calculate command with sum operation."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'sum'])
        
        assert result.exit_code == 0
        assert "Sum: 15.0" in result.output
    
    def test_calculate_mean(self):
        """Test the calculate command with mean operation."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'mean'])
        
        assert result.exit_code == 0
        assert "Mean: 3.0" in result.output
    
    def test_calculate_max(self):
        """Test the calculate command with max operation."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'max'])
        
        assert result.exit_code == 0
        assert "Max: 5.0" in result.output
    
    def test_calculate_min(self):
        """Test the calculate command with min operation."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'min'])
        
        assert result.exit_code == 0
        assert "Min: 1.0" in result.output
    
    def test_calculate_no_numbers(self):
        """Test the calculate command with no numbers."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate'])
        
        assert result.exit_code == 0
        assert "Error: No numbers provided" in result.output


class TestCliConvert:
    """Integration tests for the convert CLI command."""
    
    def test_convert_json_to_json(self, temp_json_file):
        """Test converting JSON to JSON."""
        time.sleep(0.2)
        
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            runner = CliRunner()
            result = runner.invoke(cli, ['convert', temp_json_file, output_path, '--format', 'json'])
            
            assert result.exit_code == 0
            assert f"Converted {temp_json_file} to {output_path}" in result.output
            
            # Verify the output file
            original_data = read_json_file(temp_json_file)
            converted_data = read_json_file(output_path)
            assert original_data == converted_data
            
        finally:
            # Clean up
            if os.path.exists(output_path):
                os.unlink(output_path)
    
    def test_convert_json_to_csv(self, temp_json_file):
        """Test converting JSON to CSV."""
        time.sleep(0.2)
        
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            runner = CliRunner()
            result = runner.invoke(cli, ['convert', temp_json_file, output_path, '--format', 'csv'])
            
            assert result.exit_code == 0
            assert f"Converted {temp_json_file} to {output_path}" in result.output
            
            # Verify the output file
            csv_data = read_csv_file(output_path)
            assert len(csv_data) > 0
            assert "id" in csv_data[0]
            assert "name" in csv_data[0]
            assert "value" in csv_data[0]
            
        finally:
            # Clean up
            if os.path.exists(output_path):
                os.unlink(output_path)
    
    def test_convert_csv_to_json(self, temp_csv_file):
        """Test converting CSV to JSON."""
        time.sleep(0.2)
        
        with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as output_file:
            output_path = output_file.name
        
        try:
            runner = CliRunner()
            result = runner.invoke(cli, ['convert', temp_csv_file, output_path, '--format', 'json'])
            
            assert result.exit_code == 0
            assert f"Converted {temp_csv_file} to {output_path}" in result.output
            
            # Verify the output file
            json_data = read_json_file(output_path)
            assert len(json_data) == 3  # 3 data rows (excluding header)
            assert json_data[0]["id"] == "1"
            assert json_data[0]["name"] == "Item 1"
            assert json_data[0]["value"] == "10"
            
        finally:
            # Clean up
            if os.path.exists(output_path):
                os.unlink(output_path)


class TestCliUser:
    """Integration tests for the create_user CLI command."""
    
    def test_create_user_valid(self):
        """Test creating a valid user."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-user',
            'testuser',
            'test@example.com',
            '--first-name', 'Test',
            '--last-name', 'User'
        ])
        
        assert result.exit_code == 0
        assert "User created" in result.output
        assert "testuser" in result.output
        assert "test@example.com" in result.output
        assert "Test" in result.output
        assert "User" in result.output
    
    def test_create_user_invalid(self):
        """Test creating an invalid user."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-user',
            'ab',  # Too short
            'invalid'  # No @ symbol
        ])
        
        assert result.exit_code == 0
        assert "Error:" in result.output


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
