"""Command-line interface for the slow tests demo package."""
import time
import random
import json
import click
import pandas as pd

from slow_tests_demo.utils.data_processing import process_data, clean_data
from slow_tests_demo.utils.file_operations import read_json_file, write_json_file, read_csv_file, write_csv_file
from slow_tests_demo.models.user import User
from slow_tests_demo.models.product import Product


@click.group()
def cli():
    """Slow Tests Demo CLI."""
    pass


@cli.command()
@click.argument('numbers', nargs=-1, type=float)
@click.option('--operation', '-o', type=click.Choice(['sum', 'mean', 'max', 'min']), default='sum',
              help='Operation to perform on the data.')
def calculate(numbers, operation):
    """Calculate statistics for a list of numbers."""
    time.sleep(random.uniform(0.2, 0.5))  # Artificial delay
    
    if not numbers:
        click.echo("Error: No numbers provided.")
        return
    
    result = process_data(list(numbers), operation=operation)
    click.echo(f"{operation.capitalize()}: {result}")


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--format', '-f', type=click.Choice(['json', 'csv']), default='json',
              help='File format (json or csv).')
def convert(input_file, output_file, format):
    """Convert between JSON and CSV files."""
    time.sleep(random.uniform(0.3, 0.7))  # Artificial delay
    
    # Determine input format from file extension
    input_format = 'json' if input_file.lower().endswith('.json') else 'csv'
    
    # Read input file
    if input_format == 'json':
        data = read_json_file(input_file)
        # Convert to list of lists for CSV if needed
        if format == 'csv':
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                # Get all possible keys
                keys = set()
                for item in data:
                    keys.update(item.keys())
                keys = sorted(keys)
                
                # Convert to list of lists
                csv_data = [keys]
                for item in data:
                    row = [item.get(key, '') for key in keys]
                    csv_data.append(row)
                
                write_csv_file(csv_data, output_file)
            else:
                click.echo("Error: JSON data structure not supported for CSV conversion.")
                return
        else:
            # JSON to JSON (just copy)
            write_json_file(data, output_file)
    else:  # CSV input
        data = read_csv_file(input_file)
        if format == 'json':
            # Convert to JSON
            if data:
                headers = data[0]
                json_data = []
                for row in data[1:]:
                    item = {headers[i]: value for i, value in enumerate(row) if i < len(headers)}
                    json_data.append(item)
                write_json_file(json_data, output_file)
            else:
                write_json_file([], output_file)
        else:
            # CSV to CSV (just copy)
            write_csv_file(data, output_file)
    
    click.echo(f"Converted {input_file} to {output_file}")


@cli.command()
@click.argument('username')
@click.argument('email')
@click.option('--first-name', '-f', help='User first name')
@click.option('--last-name', '-l', help='User last name')
def create_user(username, email, first_name, last_name):
    """Create a new user and print the result."""
    time.sleep(random.uniform(0.2, 0.6))  # Artificial delay
    
    try:
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.validate()
        click.echo(f"User created: {json.dumps(user.to_dict(), indent=2)}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")


@cli.command()
@click.argument('name')
@click.argument('price', type=float)
@click.option('--description', '-d', help='Product description')
@click.option('--category', '-c', help='Product category')
@click.option('--discount', type=float, help='Discount percentage to apply')
def create_product(name, price, description, category, discount):
    """Create a new product and print the result."""
    time.sleep(random.uniform(0.2, 0.6))  # Artificial delay
    
    try:
        product = Product(name=name, price=price, description=description, category=category)
        product.validate()
        
        result = product.to_dict()
        
        if discount is not None:
            discounted_price = product.apply_discount(discount)
            result['discounted_price'] = discounted_price
        
        click.echo(f"Product created: {json.dumps(result, indent=2)}")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")


if __name__ == '__main__':
    cli()
