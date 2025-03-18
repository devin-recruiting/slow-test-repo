"""Tests for data processing utilities."""
import time
import random
import pytest
import numpy as np
import pandas as pd
import os

from slow_tests_demo.utils.data_processing import process_data, transform_dataframe, clean_data


class TestProcessData:
    """Tests for the process_data function."""
    
    def test_sum_operation(self, sample_data):
        """Test sum operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        result = process_data(sample_data, operation="sum")
        expected = sum(sample_data)
        
        assert result == expected
    
    def test_mean_operation(self, sample_data):
        """Test mean operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        result = process_data(sample_data, operation="mean")
        expected = sum(sample_data) / len(sample_data)
        
        assert result == expected
    
    def test_max_operation(self, sample_data):
        """Test max operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        result = process_data(sample_data, operation="max")
        expected = max(sample_data)
        
        assert result == expected
    
    def test_min_operation(self, sample_data):
        """Test min operation."""
        # Fast test - simple calculation
        time.sleep(0.1)
        
        result = process_data(sample_data, operation="min")
        expected = min(sample_data)
        
        assert result == expected
    
    def test_invalid_operation(self, sample_data):
        """Test invalid operation."""
        # Fast test - simple validation
        time.sleep(0.1)
        
        with pytest.raises(ValueError):
            process_data(sample_data, operation="invalid")
    
    def test_with_delay(self, sample_data):
        """Test with delay parameter."""
        # Slow test - simulates database operation
        time.sleep(3.0)  # Significantly longer delay
        
        start_time = time.time()
        result = process_data(sample_data, operation="sum", delay=True)
        end_time = time.time()
        
        assert result == sum(sample_data)
        assert end_time - start_time >= 0.1  # Should have at least the minimum delay
        
    def test_large_dataset_processing(self):
        """Test processing a large dataset - very slow test."""
        # Very slow test - simulates big data processing
        time.sleep(5.0)  # Very long delay
        
        # Create a large dataset
        large_data = [random.random() * 100 for _ in range(10000)]
        
        # Test different operations
        sum_result = process_data(large_data, operation="sum")
        mean_result = process_data(large_data, operation="mean")
        max_result = process_data(large_data, operation="max")
        min_result = process_data(large_data, operation="min")
        
        # Verify results
        assert sum_result == sum(large_data)
        assert mean_result == sum(large_data) / len(large_data)
        assert max_result == max(large_data)
        assert min_result == min(large_data)


class TestTransformDataframe:
    """Tests for the transform_dataframe function."""
    
    def test_no_transformations(self, sample_dataframe):
        """Test with no transformations."""
        # Fast test - simple operation
        time.sleep(0.1)
        
        result = transform_dataframe(sample_dataframe)
        pd.testing.assert_frame_equal(result, sample_dataframe)
    
    def test_with_transformations(self, sample_dataframe):
        """Test with transformations."""
        # Fast test - simple transformations
        time.sleep(0.1)
        
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
        # Slow test - simulates complex data transformation
        time.sleep(4.0)  # Significantly longer delay
        
        start_time = time.time()
        result = transform_dataframe(sample_dataframe, delay=True)
        end_time = time.time()
        
        pd.testing.assert_frame_equal(result, sample_dataframe)
        assert end_time - start_time >= 0.2  # Should have at least the minimum delay
        
    def test_complex_dataframe_transformations(self):
        """Test complex transformations on a large dataframe - very slow test."""
        # Very slow test - simulates big data transformation
        time.sleep(6.0)  # Very long delay
        
        # Create a large dataframe
        np.random.seed(42)
        large_df = pd.DataFrame({
            'A': np.random.randint(0, 100, size=1000),
            'B': np.random.normal(50, 10, size=1000),
            'C': np.random.choice(['X', 'Y', 'Z'], size=1000),
            'D': pd.date_range(start='2020-01-01', periods=1000)
        })
        
        # Define complex transformations
        def normalize_columns(df):
            df = df.copy()
            for col in df.select_dtypes(include=['number']).columns:
                df[col] = (df[col] - df[col].mean()) / df[col].std()
            return df
            
        def add_derived_features(df):
            df = df.copy()
            df['A_squared'] = df['A'] ** 2
            df['A_B_ratio'] = df['A'] / df['B'].replace(0, 1)
            df['day_of_week'] = df['D'].dt.dayofweek
            return df
            
        def one_hot_encode(df):
            df = df.copy()
            dummies = pd.get_dummies(df['C'], prefix='category')
            return pd.concat([df, dummies], axis=1)
            
        transformations = [normalize_columns, add_derived_features, one_hot_encode]
        
        # Apply transformations
        result = transform_dataframe(large_df, transformations=transformations)
        
        # Verify results
        assert 'A_squared' in result.columns
        assert 'A_B_ratio' in result.columns
        assert 'day_of_week' in result.columns
        assert 'category_X' in result.columns
        assert 'category_Y' in result.columns
        assert 'category_Z' in result.columns
        assert result.shape[0] == 1000
        assert result.shape[1] > large_df.shape[1]


class TestCleanData:
    """Tests for the clean_data function."""
    
    def test_remove_nulls(self):
        """Test removing null values."""
        # Fast test - simple data cleaning
        time.sleep(0.1)
        
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
        # Fast test - simple data cleaning
        time.sleep(0.1)
        
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
        # Slow test - simulates complex data cleaning
        time.sleep(3.5)  # Significantly longer delay
        
        data = {'A': [1, 2, 3], 'B': [10, 20, 30]}
        df = pd.DataFrame(data)
        
        start_time = time.time()
        result = clean_data(df, delay=True)
        end_time = time.time()
        
        pd.testing.assert_frame_equal(result, df)
        assert end_time - start_time >= 0.3  # Should have at least the minimum delay
        
    def test_clean_large_messy_dataset(self):
        """Test cleaning a large messy dataset - very slow test."""
        # Very slow test - simulates cleaning big messy data
        time.sleep(7.0)  # Very long delay
        
        # Create a large messy dataframe
        np.random.seed(42)
        rows = 5000
        
        # Create data with nulls, duplicates, and outliers
        data = {
            'A': np.random.randint(0, 100, size=rows),
            'B': np.random.normal(50, 10, size=rows),
            'C': np.random.choice(['X', 'Y', 'Z'], size=rows),  # Fixed to avoid None in choice
            'D': pd.date_range(start='2020-01-01', periods=rows)
        }
        
        # Add nulls to column C manually
        null_indices = np.random.choice(rows, size=int(rows * 0.1), replace=False)
        data['C'] = pd.Series(data['C'])
        data['C'].iloc[null_indices] = None
        
        # Add some nulls
        for col in ['A', 'B']:
            null_indices = np.random.choice(rows, size=int(rows * 0.1), replace=False)
            data[col] = pd.Series(data[col])
            data[col].iloc[null_indices] = None
            
        # Add some duplicates (about 20% of the data)
        duplicate_indices = np.random.choice(rows, size=int(rows * 0.2), replace=False)
        for idx in duplicate_indices:
            duplicate_row_idx = np.random.randint(0, rows)
            for col in ['A', 'B', 'C']:
                data[col] = pd.Series(data[col])
                data[col].iloc[idx] = data[col].iloc[duplicate_row_idx]
                
        df = pd.DataFrame(data)
        
        # Clean the data
        result = clean_data(df, remove_nulls=True, remove_duplicates=True)
        
        # Verify results
        assert result.shape[0] < df.shape[0]  # Should have fewer rows
        assert not result.isnull().any().any()  # No nulls should remain
