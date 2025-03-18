from setuptools import setup, find_packages

setup(
    name="slow_tests_demo",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask>=2.3.3",
        "requests>=2.31.0",
        "numpy>=1.25.2",
        "pandas>=2.1.0",
        "click>=8.1.7",
    ],
    entry_points={
        "console_scripts": [
            "slow-demo=slow_tests_demo.cli.main:cli",
        ],
    },
)
