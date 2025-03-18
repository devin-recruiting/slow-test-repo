# Slow Tests Demo

A Python repository demonstrating a project with intentionally slow tests.

## Features

- Data processing utilities
- Simple REST API
- Command-line interface

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

Tests will run in parallel by default using pytest-xdist. To run tests sequentially, use:

```bash
pytest -n 0
```

To run specific test categories:

```bash
pytest tests/unit/
pytest tests/integration/
```
