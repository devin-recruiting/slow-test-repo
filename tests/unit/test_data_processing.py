"""Tests for data processing utilities."""
import time
import random
import pytest
import numpy as np
import pandas as pd

from slow_tests_demo.utils.data_processing import process_data, transform_dataframe, clean_data


class TestProcessData:
    """Tests for the process_data function."""
    
    def test_sum_operation(self, sample_data):
        """Test sum operation."""
        time.sleep(0.2)
        
        result = process_data(sample_data, operation="sum")
        expected = sum(sample_data)
        
        assert result == expected
    
    def test_mean_operation(self, sample_data):
        """Test mean operation."""
        time.sleep(0.2)
        
        result = process_data(sample_data, operation="mean")
        expected = sum(sample_data) / len(sample_data)
        
        assert result == expected
    
    def test_max_operation(self, sample_data):
        """Test max operation."""
        time.sleep(0.2)
        
        result = process_data(sample_data, operation="max")
        expected = max(sample_data)
        
        assert result == expected
    
    def test_min_operation(self, sample_data):
        """Test min operation."""
        time.sleep(0.2)
        
        result = process_data(sample_data, operation="min")
        expected = min(sample_data)
        
        assert result == expected
    
    def test_invalid_operation(self, sample_data):
        """Test invalid operation."""
        time.sleep(0.2)
        
        with pytest.raises(ValueError):
            process_data(sample_data, operation="invalid")
    
    def test_with_delay(self, sample_data):
        """Test with delay parameter."""
        time.sleep(0.2)
        
        start_time = time.time()
        result = process_data(sample_data, operation="sum", delay=True)
        end_time = time.time()
        
        assert result == sum(sample_data)
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay


class TestTransformDataframe:
    """Tests for the transform_dataframe function."""
    
    def test_no_transformations(self, sample_dataframe):
        """Test with no transformations."""
        time.sleep(0.2)
        
        result = transform_dataframe(sample_dataframe)
        pd.testing.assert_frame_equal(result, sample_dataframe)
    
    def test_with_transformations(self, sample_dataframe):
        """Test with transformations."""
        time.sleep(0.2)
        
        # Define some transformations
        def double_numeric(df):
            df = df.copy()
            for col in df.select_dtypes(include=['number']).columns:
                df[col] = df[col] * 2
            return df
        
        def add_column(df):
            df = df.copy()
            df['D'] = df['A'] + df['B']
            return df
        
        transformations = [double_numeric, add_column]
        
        result = transform_dataframe(sample_dataframe, transformations=transformations)
        
        # Check that original dataframe is unchanged
        assert 'D' not in sample_dataframe.columns
        
        # Check that transformations were applied
        assert 'D' in result.columns
        assert result['A'].tolist() == [2, 4, 6, 8, 10]
        assert result['B'].tolist() == [20, 40, 60, 80, 100]
        assert result['D'].tolist() == [22, 44, 66, 88, 110]
    
    def test_with_delay(self, sample_dataframe):
        """Test with delay parameter."""
        time.sleep(0.2)
        
        start_time = time.time()
        result = transform_dataframe(sample_dataframe, delay=True)
        end_time = time.time()
        
        pd.testing.assert_frame_equal(result, sample_dataframe)
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay


class TestCleanData:
    """Tests for the clean_data function."""
    
    def test_remove_nulls(self):
        """Test removing null values."""
        time.sleep(0.2)
        
        # Create a dataframe with nulls
        data = {
            'A': [1, 2, None, 4, 5],
            'B': [10, None, 30, 40, 50],
            'C': ['a', 'b', 'c', None, 'e']
        }
        df = pd.DataFrame(data)
        
        result = clean_data(df, remove_nulls=True, remove_duplicates=False)
        
        assert result.shape[0] == 2  # Only 2 rows should remain (rows 0 and 4)
        assert not result.isnull().any().any()  # No nulls should remain
    
    def test_remove_duplicates(self):
        """Test removing duplicate rows."""
        time.sleep(0.2)
        
        # Create a dataframe with duplicates
        data = {
            'A': [1, 2, 3, 1, 2],
            'B': [10, 20, 30, 10, 20],
            'C': ['a', 'b', 'c', 'a', 'b']
        }
        df = pd.DataFrame(data)
        
        result = clean_data(df, remove_nulls=False, remove_duplicates=True)
        
        assert result.shape[0] == 3  # Only 3 unique rows
    
    def test_with_delay(self):
        """Test with delay parameter."""
        time.sleep(0.2)
        
        data = {'A': [1, 2, 3], 'B': [10, 20, 30]}
        df = pd.DataFrame(data)
        
        start_time = time.time()
        result = clean_data(df, delay=True)
        end_time = time.time()
        
        pd.testing.assert_frame_equal(result, df)
        assert end_time - start_time >= 0.3  # Should have at least the minimum delay
