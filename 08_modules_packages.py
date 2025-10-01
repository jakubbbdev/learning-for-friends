# ===========================================
# MODULES AND PACKAGES - Organizing and Reusing Code
# ===========================================

print("=== MODULES AND PACKAGES ===")

# WHAT ARE MODULES?
# A module is a Python file containing functions, classes, and variables
# Modules help organize code and make it reusable

# BUILT-IN MODULES
print("\n--- Built-in Modules ---")

# Import entire module
import math
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")

# Import specific functions
from datetime import datetime, timedelta
now = datetime.now()
print(f"Current time: {now}")
print(f"Time 7 days ago: {now - timedelta(days=7)}")

# Import with alias
import random as rnd
print(f"Random number: {rnd.randint(1, 100)}")
print(f"Random choice: {rnd.choice(['apple', 'banana', 'orange'])}")

# Import multiple items
from os import path, listdir
print(f"Current directory: {path.getcwd()}")
print(f"Files in current directory: {len(listdir('.'))}")

# WORKING WITH CUSTOM MODULES
print("\n--- Creating Custom Modules ---")

# Let's create a simple math utilities module
# This would normally be in a separate file called 'math_utils.py'

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Constants
PI = 3.14159
E = 2.71828

# This is how you would import it:
# import math_utils
# from math_utils import add_numbers, factorial
# from math_utils import PI as MATH_PI

print("Custom math utilities:")
print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"4 * 7 = {multiply_numbers(4, 7)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Factorial of 5: {factorial(5)}")

# WORKING WITH PACKAGES
print("\n--- Understanding Packages ---")

# A package is a collection of modules organized in directories
# Packages have an __init__.py file (can be empty)

# Example package structure:
# my_package/
#     __init__.py
#     math_utils.py
#     string_utils.py
#     data_utils.py

# Example of what would be in __init__.py:
"""
# This makes functions available when importing the package
from .math_utils import add_numbers, multiply_numbers
from .string_utils import reverse_string, count_words
from .data_utils import save_to_file, load_from_file

# Define what gets imported with "from my_package import *"
__all__ = [
    'add_numbers', 'multiply_numbers',
    'reverse_string', 'count_words',
    'save_to_file', 'load_from_file'
]
"""

# STANDARD LIBRARY EXAMPLES
print("\n--- Standard Library Examples ---")

# Collections module - Advanced data structures
from collections import Counter, defaultdict, namedtuple

# Counter - Count occurrences of elements
text = "hello world hello python world hello"
word_count = Counter(text.split())
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# Defaultdict - Dictionary with default values
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')
print(f"Default dict: {dict(dd)}")

# Namedtuple - Tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"Point 1: {p1}, Point 2: {p2}")
print(f"Distance: {((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5}")

# JSON module - Working with JSON data
import json

# Python dictionary to JSON
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"],
    "married": False
}

json_string = json.dumps(data, indent=2)
print(f"JSON string:\n{json_string}")

# JSON to Python dictionary
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")

# Requests module (if installed) - HTTP requests
# import requests
# response = requests.get('https://api.github.com/users/octocat')
# print(response.json())

# WORKING WITH FILES AS MODULES
print("\n--- File-based Module Example ---")

# Let's create a simple configuration module
config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retries": 3
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

# This would be in config.py
def get_config():
    """Get application configuration"""
    return config_data

def get_database_config():
    """Get database configuration"""
    return config_data["database"]

def get_api_config():
    """Get API configuration"""
    return config_data["api"]

# Using the config
print("Configuration example:")
print(f"Database host: {get_database_config()['host']}")
print(f"API timeout: {get_api_config()['timeout']} seconds")

# RELATIVE IMPORTS (for packages)
print("\n--- Relative Imports ---")

# In a package, you can use relative imports:
# from .module_name import function_name  # Same package
# from ..parent_package import function_name  # Parent package
# from .subpackage import function_name  # Subpackage

# Example package structure:
"""
my_project/
    __init__.py
    main.py
    utils/
        __init__.py
        math_utils.py
        string_utils.py
    models/
        __init__.py
        user.py
        product.py
"""

# DYNAMIC IMPORTS
print("\n--- Dynamic Imports ---")

def load_module_dynamically(module_name):
    """Dynamically import a module"""
    try:
        module = __import__(module_name)
        return module
    except ImportError:
        print(f"Module '{module_name}' not found")
        return None

# Test dynamic import
math_module = load_module_dynamically('math')
if math_module:
    print(f"Math module loaded: {math_module.sqrt(25)}")

# IMPORTING WITH CONDITIONS
print("\n--- Conditional Imports ---")

# Try to import optional modules
try:
    import numpy as np
    print("NumPy is available")
    numpy_available = True
except ImportError:
    print("NumPy is not installed")
    numpy_available = False

try:
    import pandas as pd
    print("Pandas is available")
    pandas_available = True
except ImportError:
    print("Pandas is not installed")
    pandas_available = False

# Use conditional imports
if numpy_available:
    print("Using NumPy for calculations")
    # array = np.array([1, 2, 3, 4, 5])
else:
    print("Using built-in Python for calculations")
    # array = [1, 2, 3, 4, 5]

# MODULE ATTRIBUTES
print("\n--- Module Attributes ---")

# Every module has special attributes
print(f"Math module name: {math.__name__}")
print(f"Math module file: {math.__file__}")
print(f"Math module doc: {math.__doc__}")

# List all attributes of a module
print("Math module attributes:")
for attr in dir(math):
    if not attr.startswith('_'):  # Skip private attributes
        print(f"  {attr}")

# CREATING A SIMPLE PACKAGE STRUCTURE
print("\n--- Creating Package Structure ---")

# This demonstrates how to create a simple package
# In practice, you would create these as separate files

# my_utils/__init__.py
package_init_content = '''
"""
My Utils Package

A collection of utility functions for common tasks.
"""

from .math_utils import add_numbers, multiply_numbers, factorial
from .string_utils import reverse_string, count_words, clean_text
from .file_utils import read_file, write_file, append_to_file

__version__ = "1.0.0"
__author__ = "Python Learner"

# What gets imported with "from my_utils import *"
__all__ = [
    'add_numbers', 'multiply_numbers', 'factorial',
    'reverse_string', 'count_words', 'clean_text',
    'read_file', 'write_file', 'append_to_file'
]
'''

# my_utils/math_utils.py
math_utils_content = '''
"""Mathematical utility functions."""

def add_numbers(a, b):
    """Add two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b

def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        return None
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
'''

# my_utils/string_utils.py
string_utils_content = '''
"""String utility functions."""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_words(text):
    """Count words in a text."""
    return len(text.split())

def clean_text(text):
    """Clean text by removing extra whitespace."""
    return ' '.join(text.split())
'''

print("Package structure created (conceptually):")
print("my_utils/")
print("├── __init__.py")
print("├── math_utils.py")
print("└── string_utils.py")

# PRACTICAL EXAMPLE: Simple Calculator Package
print("\n--- Practical Example: Calculator Package ---")

class SimpleCalculator:
    """A simple calculator class"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()

# Using the calculator
calc = SimpleCalculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")

print("Calculation history:")
for calculation in calc.get_history():
    print(f"  {calculation}")

# MODULE SEARCH PATH
print("\n--- Module Search Path ---")

import sys
print("Python searches for modules in these locations:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# BEST PRACTICES
print("\n=== MODULE AND PACKAGE BEST PRACTICES ===")
print("1. Use descriptive module and package names")
print("2. Keep modules focused on a single purpose")
print("3. Use __init__.py to control what gets imported")
print("4. Document your modules with docstrings")
print("5. Use relative imports within packages")
print("6. Handle ImportError exceptions gracefully")
print("7. Use virtual environments for project dependencies")
print("8. Follow PEP 8 naming conventions")
print("9. Use __all__ to control 'from module import *'")
print("10. Keep module files reasonably sized")
