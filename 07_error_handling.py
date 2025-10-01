ja # ===========================================
# ERROR HANDLING AND EXCEPTIONS - Dealing with Problems
# ===========================================

print("=== ERROR HANDLING AND EXCEPTIONS ===")

# WHAT ARE EXCEPTIONS?
# Exceptions are errors that occur during program execution
# Python has many built-in exception types for different kinds of errors

# BASIC TRY-EXCEPT BLOCK
print("\n--- Basic Try-Except ---")

try:
    # This code might cause an error
    result = 10 / 0  # This will cause a ZeroDivisionError
    print(f"Result: {result}")
except ZeroDivisionError:
    # This code runs if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero!")
    print("The program continues running instead of crashing")

print("Program continues after the error handling")

# HANDLING MULTIPLE EXCEPTION TYPES
print("\n--- Multiple Exception Types ---")

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers!")
        return None

# Test the function with different inputs
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'hello' = {safe_divide(10, 'hello')}")

# TRY-EXCEPT-ELSE-FINALLY
print("\n--- Try-Except-Else-Finally ---")

def read_file_safely(filename):
    """Demonstrate try-except-else-finally blocks"""
    file_handle = None
    try:
        # Try to open and read the file
        file_handle = open(filename, 'r')
        content = file_handle.read()
        print(f"Successfully read {len(content)} characters from {filename}")
        
    except FileNotFoundError:
        # This runs if the file doesn't exist
        print(f"Error: File '{filename}' not found!")
        return None
        
    except PermissionError:
        # This runs if we don't have permission to read the file
        print(f"Error: Permission denied to read '{filename}'!")
        return None
        
    except Exception as e:
        # This catches any other unexpected errors
        print(f"Unexpected error: {type(e).__name__}: {e}")
        return None
        
    else:
        # This runs only if no exception occurred
        print("File reading completed successfully!")
        return content
        
    finally:
        # This always runs, whether there was an exception or not
        if file_handle:
            file_handle.close()
            print("File handle closed")

# Test with different scenarios
read_file_safely("nonexistent.txt")  # FileNotFoundError
read_file_safely("07_error_handling.py")  # Should work

# RAISING EXCEPTIONS
print("\n--- Raising Exceptions ---")

def validate_age(age):
    """Validate age and raise custom exceptions"""
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    
    if age > 150:
        raise ValueError("Age seems unrealistic (over 150)")
    
    return True

# Test the validation function
test_ages = [25, -5, "twenty", 200, 0, 30]

for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age} is valid")
    except TypeError as e:
        print(f"Type error for age {age}: {e}")
    except ValueError as e:
        print(f"Value error for age {age}: {e}")

# CUSTOM EXCEPTION CLASSES
print("\n--- Custom Exception Classes ---")

class CustomError(Exception):
    """Base class for custom exceptions"""
    pass

class InvalidEmailError(CustomError):
    """Raised when email format is invalid"""
    def __init__(self, email):
        self.email = email
        super().__init__(f"Invalid email format: {email}")

class UserNotFoundError(CustomError):
    """Raised when user is not found"""
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"User with ID {user_id} not found")

def validate_email(email):
    """Validate email format"""
    if "@" not in email or "." not in email.split("@")[1]:
        raise InvalidEmailError(email)
    return True

def find_user(user_id):
    """Simulate finding a user"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    if user_id not in users:
        raise UserNotFoundError(user_id)
    return users[user_id]

# Test custom exceptions
test_emails = ["alice@email.com", "invalid-email", "bob@domain.co.uk"]
test_user_ids = [1, 5, 2]

print("Testing email validation:")
for email in test_emails:
    try:
        validate_email(email)
        print(f"✓ {email} is valid")
    except InvalidEmailError as e:
        print(f"✗ {e}")

print("\nTesting user lookup:")
for user_id in test_user_ids:
    try:
        user = find_user(user_id)
        print(f"✓ Found user: {user}")
    except UserNotFoundError as e:
        print(f"✗ {e}")

# ASSERT STATEMENTS
print("\n--- Assert Statements ---")

def calculate_average(numbers):
    """Calculate average with assertions"""
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    
    return sum(numbers) / len(numbers)

# Test assertions
test_lists = [
    [1, 2, 3, 4, 5],
    [],  # This will trigger an assertion error
    [1, 2, "three", 4]  # This will also trigger an assertion error
]

for numbers in test_lists:
    try:
        avg = calculate_average(numbers)
        print(f"Average of {numbers} is {avg}")
    except AssertionError as e:
        print(f"Assertion failed for {numbers}: {e}")

# CONTEXT MANAGERS (with statement)
print("\n--- Context Managers ---")

class FileManager:
    """Custom context manager for file operations"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering the 'with' block"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the 'with' block"""
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        # Handle any exceptions that occurred
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        
        return False  # Don't suppress the exception

# Using the custom context manager
try:
    with FileManager("test_file.txt", "w") as f:
        f.write("This is a test file\n")
        f.write("Created with custom context manager\n")
        # Simulate an error
        # raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught error outside context manager: {e}")

# Using built-in context managers
print("\nUsing built-in context manager:")
with open("context_test.txt", "w") as f:
    f.write("This file will be automatically closed\n")
    f.write("Even if an exception occurs\n")

# ERROR HANDLING IN LOOPS
print("\n--- Error Handling in Loops ---")

def process_numbers(numbers):
    """Process a list of numbers, handling errors gracefully"""
    results = []
    
    for i, num in enumerate(numbers):
        try:
            # Simulate some processing that might fail
            if isinstance(num, str):
                # Try to convert string to number
                processed = float(num)
            else:
                processed = float(num)
            
            # Simulate division that might fail
            result = 100 / processed
            results.append(result)
            print(f"✓ Processed {num} -> {result}")
            
        except ValueError:
            print(f"✗ Cannot convert '{num}' to number (position {i})")
            results.append(None)
            
        except ZeroDivisionError:
            print(f"✗ Cannot divide by zero: {num} (position {i})")
            results.append(None)
            
        except Exception as e:
            print(f"✗ Unexpected error processing {num}: {e}")
            results.append(None)
    
    return results

# Test with various inputs
test_numbers = [10, 0, "25.5", "hello", -5, 2.5, None]
results = process_numbers(test_numbers)
print(f"Results: {results}")

# LOGGING ERRORS
print("\n--- Logging Errors ---")

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error_log.txt'),
        logging.StreamHandler()  # Also print to console
    ]
)

def risky_operation(x):
    """An operation that might fail"""
    try:
        if x < 0:
            raise ValueError("Negative values not allowed")
        result = x ** 0.5  # Square root
        logging.info(f"Successfully calculated sqrt({x}) = {result}")
        return result
    except ValueError as e:
        logging.error(f"ValueError in risky_operation: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error in risky_operation: {e}")
        return None

# Test logging
test_values = [16, -4, 25, "hello", 9]
for value in test_values:
    result = risky_operation(value)

print("Check 'error_log.txt' file for logged errors")

# BEST PRACTICES SUMMARY
print("\n=== ERROR HANDLING BEST PRACTICES ===")
print("1. Always use specific exception types when possible")
print("2. Don't use bare 'except:' clauses - catch specific exceptions")
print("3. Use 'finally' blocks for cleanup operations")
print("4. Log errors for debugging purposes")
print("5. Don't ignore exceptions - handle them appropriately")
print("6. Use assertions for debugging, not for production error handling")
print("7. Create custom exceptions for your specific use cases")
print("8. Use context managers for resource management")

# PRACTICAL EXAMPLE: Robust Calculator
print("\n--- Practical Example: Robust Calculator ---")

class RobustCalculator:
    """A calculator with comprehensive error handling"""
    
    def __init__(self):
        self.history = []
    
    def safe_calculate(self, operation, a, b):
        """Safely perform a calculation with error handling"""
        try:
            # Validate inputs
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("Both operands must be numbers")
            
            # Perform operation
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = a / b
            elif operation == "power":
                result = a ** b
            else:
                raise ValueError(f"Unknown operation: {operation}")
            
            # Record successful calculation
            self.history.append({
                "operation": operation,
                "operands": (a, b),
                "result": result,
                "success": True
            })
            
            return result
            
        except (TypeError, ZeroDivisionError, ValueError) as e:
            # Record failed calculation
            self.history.append({
                "operation": operation,
                "operands": (a, b),
                "error": str(e),
                "success": False
            })
            
            print(f"Calculation error: {e}")
            return None
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()

# Test the robust calculator
calc = RobustCalculator()

test_calculations = [
    ("add", 5, 3),
    ("divide", 10, 0),
    ("multiply", "5", 3),
    ("power", 2, 8),
    ("unknown", 1, 2)
]

for operation, a, b in test_calculations:
    result = calc.safe_calculate(operation, a, b)
    if result is not None:
        print(f"{a} {operation} {b} = {result}")

print(f"\nCalculation history: {len(calc.get_history())} entries")
for entry in calc.get_history():
    if entry["success"]:
        print(f"✓ {entry['operands'][0]} {entry['operation']} {entry['operands'][1]} = {entry['result']}")
    else:
        print(f"✗ {entry['operands'][0]} {entry['operation']} {entry['operands'][1]}: {entry['error']}")
