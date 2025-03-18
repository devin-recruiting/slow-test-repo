"""File operation utilities."""
import os
import time
import random
import json
import csv


def read_json_file(filepath, delay=False):
    """
    Read a JSON file with optional delay.
    
    Args:
        filepath: Path to the JSON file
        delay: Whether to add an artificial delay
        
    Returns:
        Parsed JSON data
    """
    if delay:
        time.sleep(random.uniform(0.2, 0.6))
    
    with open(filepath, 'r') as f:
        return json.load(f)


def write_json_file(data, filepath, delay=False):
    """
    Write data to a JSON file with optional delay.
    
    Args:
        data: Data to write
        filepath: Path to the JSON file
        delay: Whether to add an artificial delay
    """
    if delay:
        time.sleep(random.uniform(0.2, 0.5))
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def read_csv_file(filepath, delimiter=',', delay=False):
    """
    Read a CSV file with optional delay.
    
    Args:
        filepath: Path to the CSV file
        delimiter: CSV delimiter
        delay: Whether to add an artificial delay
        
    Returns:
        List of rows from the CSV file
    """
    if delay:
        time.sleep(random.uniform(0.3, 0.7))
    
    rows = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            rows.append(row)
    
    return rows


def write_csv_file(data, filepath, delimiter=',', delay=False):
    """
    Write data to a CSV file with optional delay.
    
    Args:
        data: List of rows to write
        filepath: Path to the CSV file
        delimiter: CSV delimiter
        delay: Whether to add an artificial delay
    """
    if delay:
        time.sleep(random.uniform(0.2, 0.6))
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)
