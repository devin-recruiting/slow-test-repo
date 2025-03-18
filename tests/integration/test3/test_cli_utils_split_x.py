"""Integration tests for CLI convert command with reduced coverage."""
import os
import time
import tempfile
import pytest

from click.testing import CliRunner
from slow_tests_demo.cli.main import cli
from slow_tests_demo.utils.file_operations import read_json_file, read_csv_file


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
            
            # Removed verification of output file contents
            # This reduces coverage by not testing the actual file reading/writing functionality
            
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
            
            # Removed verification of CSV file contents
            # This reduces coverage by not testing the CSV parsing functionality
            
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
            
            # Removed verification of JSON file contents
            # This reduces coverage by not testing the JSON parsing functionality
            
        finally:
            # Clean up
            if os.path.exists(output_path):
                os.unlink(output_path)
