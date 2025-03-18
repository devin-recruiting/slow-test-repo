"""Data processing utilities."""
import time
import random
import numpy as np
import pandas as pd


def process_data(data, operation="sum", delay=False):
    """
    Process data with an optional artificial delay.
    
    Args:
        data: List or numpy array of numeric data
        operation: Operation to perform (sum, mean, max, min)
        delay: Whether to add an artificial delay
        
    Returns:
        Processed result
    """
    if delay:
        time.sleep(random.uniform(0.1, 0.5))
    
    data = np.array(data)
    
    if operation == "sum":
        return np.sum(data)
    elif operation == "mean":
        return np.mean(data)
    elif operation == "max":
        return np.max(data)
    elif operation == "min":
        return np.min(data)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def transform_dataframe(df, transformations=None, delay=False):
    """
    Apply transformations to a pandas DataFrame with optional delay.
    
    Args:
        df: pandas DataFrame
        transformations: List of transformation functions to apply
        delay: Whether to add an artificial delay
        
    Returns:
        Transformed DataFrame
    """
    if delay:
        time.sleep(random.uniform(0.2, 0.7))
    
    if transformations is None:
        return df
    
    result = df.copy()
    for transform in transformations:
        result = transform(result)
    
    return result


def clean_data(data, remove_nulls=True, remove_duplicates=True, delay=False):
    """
    Clean a pandas DataFrame by removing nulls and/or duplicates.
    
    Args:
        data: pandas DataFrame
        remove_nulls: Whether to remove null values
        remove_duplicates: Whether to remove duplicate rows
        delay: Whether to add an artificial delay
        
    Returns:
        Cleaned DataFrame
    """
    if delay:
        time.sleep(random.uniform(0.3, 0.8))
    
    result = data.copy()
    
    if remove_nulls:
        result = result.dropna()
    
    if remove_duplicates:
        result = result.drop_duplicates()
    
    return result
