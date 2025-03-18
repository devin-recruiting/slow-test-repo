"""Integration tests for CLI calculate command."""
import time
from click.testing import CliRunner
import pytest

from slow_tests_demo.cli.main import cli


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
