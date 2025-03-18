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
        # Fast test - simple calculation
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'sum'])
        
        assert result.exit_code == 0
        assert "Sum: 15.0" in result.output
    
    def test_calculate_mean(self):
        """Test the calculate command with mean operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'mean'])
        
        assert result.exit_code == 0
        assert "Mean: 3.0" in result.output
    
    def test_calculate_max(self):
        """Test the calculate command with max operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'max'])
        
        assert result.exit_code == 0
        assert "Max: 5.0" in result.output
    
    def test_calculate_min(self):
        """Test the calculate command with min operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate', '1', '2', '3', '4', '5', '--operation', 'min'])
        
        assert result.exit_code == 0
        assert "Min: 1.0" in result.output
    
    def test_calculate_no_numbers(self):
        """Test the calculate command with no numbers."""
        # Fast test - error handling
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate'])
        
        assert result.exit_code == 0
        assert "Error: No numbers provided" in result.output
        
    def test_calculate_large_dataset(self):
        """Test the calculate command with a large dataset - slow test."""
        # Slow test - simulates processing large data
        time.sleep(4.0)  # Significantly longer delay
        
        # Generate a large dataset
        numbers = [str(random.uniform(1, 100)) for _ in range(1000)]
        
        runner = CliRunner()
        result = runner.invoke(cli, ['calculate'] + numbers + ['--operation', 'sum'])
        
        assert result.exit_code == 0
        assert "Sum:" in result.output
        
        # Also test mean on large dataset
        result = runner.invoke(cli, ['calculate'] + numbers + ['--operation', 'mean'])
        assert result.exit_code == 0
        assert "Mean:" in result.output


class TestCliConvert:
    """Integration tests for the convert CLI command."""
    
    def test_convert_json_to_json(self, temp_json_file):
        """Test converting JSON to JSON."""
        # Fast test - simple file conversion
        time.sleep(0.1)
        
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
        # Fast test - simple file conversion
        time.sleep(0.1)
        
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
        # Fast test - simple file conversion
        time.sleep(0.1)
        
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
                
    def test_convert_large_files(self, tmpdir):
        """Test converting large files - very slow test."""
        # Very slow test - simulates processing large files
        time.sleep(5.5)  # Very long delay
        
        # Create a large JSON file
        large_json_path = os.path.join(tmpdir, "large.json")
        large_csv_path = os.path.join(tmpdir, "large.csv")
        
        # Generate large dataset
        large_data = []
        for i in range(2000):
            large_data.append({
                "id": i,
                "name": f"Item {i}",
                "value": random.randint(1, 1000),
                "category": random.choice(["A", "B", "C", "D", "E"]),
                "date": f"2023-{random.randint(1, 12)}-{random.randint(1, 28)}"
            })
            
        # Write to JSON file
        with open(large_json_path, 'w') as f:
            json.dump(large_data, f)
            
        try:
            # Convert JSON to CSV
            runner = CliRunner()
            result = runner.invoke(cli, ['convert', large_json_path, large_csv_path, '--format', 'csv'])
            
            assert result.exit_code == 0
            assert f"Converted {large_json_path} to {large_csv_path}" in result.output
            
            # Verify CSV file was created
            assert os.path.exists(large_csv_path)
            
            # Convert back to JSON
            result = runner.invoke(cli, ['convert', large_csv_path, large_json_path, '--format', 'json'])
            
            assert result.exit_code == 0
            assert f"Converted {large_csv_path} to {large_json_path}" in result.output
            
            # Verify JSON file was created
            assert os.path.exists(large_json_path)
            
        finally:
            # Clean up
            if os.path.exists(large_json_path):
                os.unlink(large_json_path)
            if os.path.exists(large_csv_path):
                os.unlink(large_csv_path)


class TestCliUser:
    """Integration tests for the create_user CLI command."""
    
    def test_create_user_valid(self):
        """Test creating a valid user."""
        # Fast test - simple user creation
        time.sleep(0.1)
        
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
        # Fast test - validation error
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-user',
            'ab',  # Too short
            'invalid'  # No @ symbol
        ])
        
        assert result.exit_code == 0
        assert "Error:" in result.output
        
    def test_create_bulk_users(self):
        """Test creating multiple users in bulk - very slow test."""
        # Very slow test - simulates batch processing
        time.sleep(6.0)  # Very long delay
        
        # Create multiple users
        runner = CliRunner()
        
        # Generate user data
        first_names = ["John", "Jane", "Bob", "Alice", "Charlie"]
        last_names = ["Smith", "Doe", "Johnson", "Brown", "Wilson"]
        
        for i in range(50):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            username = f"{first_name.lower()}{last_name.lower()}{i}"
            email = f"{username}@example.com"
            
            result = runner.invoke(cli, [
                'create-user',
                username,
                email,
                '--first-name', first_name,
                '--last-name', last_name
            ])
            
            assert result.exit_code == 0
            assert "User created" in result.output
            assert username in result.output
            assert email in result.output


class TestCliProduct:
    """Integration tests for the create_product CLI command."""
    
    def test_create_product_valid(self):
        """Test creating a valid product."""
        # Fast test - simple product creation
        time.sleep(0.1)
        
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
        # Slow test - discount calculation
        time.sleep(3.0)  # Significantly longer delay
        
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
        # Fast test - validation error
        time.sleep(0.1)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-product',
            'A',  # Too short
            '-10.0'  # Negative price
        ])
        
        # CLI returns non-zero exit code for invalid input
        assert "Error:" in result.output
        
    def test_create_bulk_products(self):
        """Test creating multiple products in bulk - very slow test."""
        # Very slow test - simulates batch processing
        time.sleep(5.0)  # Very long delay
        
        # Create multiple products
        runner = CliRunner()
        
        # Generate product data
        categories = ["Electronics", "Clothing", "Food", "Books", "Toys"]
        
        for i in range(50):
            name = f"Bulk Product {i}"
            price = random.uniform(10.0, 1000.0)
            category = random.choice(categories)
            description = f"This is bulk product {i} in the {category} category"
            
            result = runner.invoke(cli, [
                'create-product',
                name,
                str(price),
                '--description', description,
                '--category', category
            ])
            
            assert result.exit_code == 0
            assert "Product created" in result.output
            assert name in result.output
            assert category in result.output
