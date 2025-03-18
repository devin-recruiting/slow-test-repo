"""Tests for file operation utilities."""
import os
import time
import random
import json
import pytest

from slow_tests_demo.utils.file_operations import read_json_file, write_json_file, read_csv_file, write_csv_file


class TestJsonOperations:
    """Tests for JSON file operations."""
    
    def test_read_json_file(self, temp_json_file):
        """Test reading a JSON file."""
        # Fast test - simple file read
        time.sleep(0.1)
        
        data = read_json_file(temp_json_file)
        
        assert isinstance(data, list)
        assert len(data) == 3
        assert data[0]["id"] == 1
        assert data[1]["name"] == "Item 2"
        assert data[2]["value"] == 30
    
    def test_write_json_file(self, tmpdir):
        """Test writing a JSON file."""
        # Fast test - simple file write
        time.sleep(0.1)
        
        data = [
            {"id": 1, "name": "Test 1", "value": 100},
            {"id": 2, "name": "Test 2", "value": 200}
        ]
        
        filepath = os.path.join(tmpdir, "test.json")
        write_json_file(data, filepath)
        
        # Verify the file was written correctly
        with open(filepath, 'r') as f:
            written_data = json.load(f)
        
        assert written_data == data
    
    def test_read_with_delay(self, temp_json_file):
        """Test reading a JSON file with delay."""
        # Slow test - simulates network file read
        time.sleep(3.0)  # Significantly longer delay
        
        start_time = time.time()
        data = read_json_file(temp_json_file, delay=True)
        end_time = time.time()
        
        assert isinstance(data, list)
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
    
    def test_write_with_delay(self, tmpdir):
        """Test writing a JSON file with delay."""
        # Slow test - simulates network file write
        time.sleep(2.5)  # Significantly longer delay
        
        data = [{"id": 1, "name": "Test", "value": 100}]
        filepath = os.path.join(tmpdir, "test_delay.json")
        
        start_time = time.time()
        write_json_file(data, filepath, delay=True)
        end_time = time.time()
        
        assert os.path.exists(filepath)
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
        
    def test_large_json_operations(self, tmpdir):
        """Test operations on large JSON files - very slow test."""
        # Very slow test - simulates big data file operations
        time.sleep(5.0)  # Very long delay
        
        # Create a large JSON dataset
        large_data = []
        for i in range(1000):
            large_data.append({
                "id": i,
                "name": f"Item {i}",
                "value": random.randint(1, 1000),
                "tags": [f"tag{j}" for j in range(random.randint(1, 5))],
                "metadata": {
                    "created_at": f"2023-{random.randint(1, 12)}-{random.randint(1, 28)}",
                    "updated_at": f"2023-{random.randint(1, 12)}-{random.randint(1, 28)}",
                    "version": random.randint(1, 10)
                }
            })
            
        # Write large dataset to file
        filepath = os.path.join(tmpdir, "large_data.json")
        write_json_file(large_data, filepath)
        
        # Read it back
        read_data = read_json_file(filepath)
        
        # Verify
        assert len(read_data) == 1000
        assert read_data[0]["id"] == 0
        assert read_data[999]["id"] == 999


class TestCsvOperations:
    """Tests for CSV file operations."""
    
    def test_read_csv_file(self, temp_csv_file):
        """Test reading a CSV file."""
        # Fast test - simple file read
        time.sleep(0.1)
        
        rows = read_csv_file(temp_csv_file)
        
        assert isinstance(rows, list)
        assert len(rows) == 4  # Header + 3 data rows
        assert rows[0] == ["id", "name", "value"]
        assert rows[1] == ["1", "Item 1", "10"]
        assert rows[2] == ["2", "Item 2", "20"]
        assert rows[3] == ["3", "Item 3", "30"]
    
    def test_write_csv_file(self, tmpdir):
        """Test writing a CSV file."""
        # Fast test - simple file write
        time.sleep(0.1)
        
        data = [
            ["id", "name", "value"],
            ["1", "Test 1", "100"],
            ["2", "Test 2", "200"]
        ]
        
        filepath = os.path.join(tmpdir, "test.csv")
        write_csv_file(data, filepath)
        
        # Verify the file was written correctly
        written_data = read_csv_file(filepath)
        assert written_data == data
    
    def test_read_with_delay(self, temp_csv_file):
        """Test reading a CSV file with delay."""
        # Slow test - simulates network file read
        time.sleep(3.5)  # Significantly longer delay
        
        start_time = time.time()
        rows = read_csv_file(temp_csv_file, delay=True)
        end_time = time.time()
        
        assert isinstance(rows, list)
        assert end_time - start_time >= 0.3  # Should have at least the minimum delay
    
    def test_write_with_delay(self, tmpdir):
        """Test writing a CSV file with delay."""
        # Slow test - simulates network file write
        time.sleep(4.0)  # Significantly longer delay
        
        data = [
            ["id", "name", "value"],
            ["1", "Test", "100"]
        ]
        filepath = os.path.join(tmpdir, "test_delay.csv")
        
        start_time = time.time()
        write_csv_file(data, filepath, delay=True)
        end_time = time.time()
        
        assert os.path.exists(filepath)
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
        
    def test_large_csv_operations(self, tmpdir):
        """Test operations on large CSV files - very slow test."""
        # Very slow test - simulates big data file operations
        time.sleep(6.0)  # Very long delay
        
        # Create a large CSV dataset
        large_data = [["id", "name", "value", "category", "date"]]
        for i in range(2000):
            large_data.append([
                str(i),
                f"Product {i}",
                str(random.randint(10, 1000)),
                random.choice(["A", "B", "C", "D", "E"]),
                f"2023-{random.randint(1, 12)}-{random.randint(1, 28)}"
            ])
            
        # Write large dataset to file
        filepath = os.path.join(tmpdir, "large_data.csv")
        write_csv_file(large_data, filepath)
        
        # Read it back
        read_data = read_csv_file(filepath)
        
        # Verify
        assert len(read_data) == 2001  # Header + 2000 rows
        assert read_data[0] == ["id", "name", "value", "category", "date"]
        assert read_data[1][0] == "0"
        assert read_data[2000][0] == "1999"
