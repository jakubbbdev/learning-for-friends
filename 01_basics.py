# ===========================================
# PYTHON BASICS - Getting Started
# ===========================================

# This is a comment - Python ignores everything after the # symbol
# Comments are used to explain what the code does

print("Hello, World!")  # print() displays text on the screen

# Variables store data
name = "Alice"  # String (text) variable
age = 25        # Integer (whole number) variable
height = 5.6    # Float (decimal number) variable
is_student = True  # Boolean (True/False) variable

# You can print variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# Basic math operations
a = 10
b = 3

print("Addition:", a + b)      # 10 + 3 = 13
print("Subtraction:", a - b)   # 10 - 3 = 7
print("Multiplication:", a * b)  # 10 * 3 = 30
print("Division:", a / b)      # 10 / 3 = 3.333...
print("Floor division:", a // b)  # 10 // 3 = 3 (integer division)
print("Modulo:", a % b)        # 10 % 3 = 1 (remainder)
print("Power:", a ** b)        # 10 ** 3 = 1000 (10 to the power of 3)

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print("Full name:", full_name)

# String formatting (different ways)
print(f"Hello, {first_name}!")  # f-string (modern way)
print("Hello, {}!".format(first_name))  # .format() method
print("Hello, %s!" % first_name)  # % formatting (older way)

# Getting user input
user_input = input("What's your name? ")
print(f"Nice to meet you, {user_input}!")

# Converting between data types
number_as_string = "42"
number_as_int = int(number_as_string)    # Convert string to integer
number_as_float = float(number_as_string)  # Convert string to float
string_from_number = str(42)             # Convert number to string

print(f"String: {number_as_string}, Integer: {number_as_int}, Float: {number_as_float}")
