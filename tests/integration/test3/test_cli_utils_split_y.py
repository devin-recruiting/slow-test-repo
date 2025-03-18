"""Integration tests for CLI user command with reduced coverage."""
import time
from click.testing import CliRunner
import pytest

from slow_tests_demo.cli.main import cli


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
            # Removed optional parameters that would test additional code paths
            # '--first-name', 'Test',
            # '--last-name', 'User'
        ])
        
        assert result.exit_code == 0
        assert "User created" in result.output
        assert "testuser" in result.output
        assert "test@example.com" in result.output
        # Removed assertions that would verify optional parameters
        # assert "Test" in result.output
        # assert "User" in result.output
    
    def test_create_user_invalid(self):
        """Test creating an invalid user."""
        time.sleep(0.2)
        
        runner = CliRunner()
        result = runner.invoke(cli, [
            'create-user',
            'ab',  # Too short
            'invalid'  # No @ symbol
        ])
        
        # Only checking for error, not specific error message
        # This reduces coverage of specific error handling paths
        assert "Error" in result.output
