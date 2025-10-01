# ===========================================
# FUNCTIONS AND CLASSES - Reusable Code and Object-Oriented Programming
# ===========================================

# FUNCTIONS - Reusable blocks of code
print("=== FUNCTIONS ===")

# Basic function definition
def greet():
    """This is a docstring - it explains what the function does"""
    print("Hello, World!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Function with default parameters
def greet_with_title(name, title="Mr."):
    """Greet someone with an optional title"""
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))  # Uses default title
print(greet_with_title("Johnson", "Dr."))  # Uses custom title
print(greet_with_title("Davis", title="Ms."))  # Named parameter

# Function with keyword arguments
def create_profile(name, age, city="Unknown", occupation="Unknown"):
    """Create a user profile"""
    return {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation
    }

# Different ways to call the function
profile1 = create_profile("Alice", 25)
profile2 = create_profile("Bob", 30, city="New York")
profile3 = create_profile("Charlie", 35, occupation="Engineer", city="San Francisco")

print(f"Profile 1: {profile1}")
print(f"Profile 2: {profile2}")
print(f"Profile 3: {profile3}")

# Function with variable number of arguments
def calculate_average(*numbers):
    """Calculate the average of any number of numbers"""
    if not numbers:  # Check if no numbers provided
        return 0
    return sum(numbers) / len(numbers)

print(f"Average of 1,2,3: {calculate_average(1, 2, 3)}")
print(f"Average of 10,20,30,40: {calculate_average(10, 20, 30, 40)}")
print(f"Average of no numbers: {calculate_average()}")

# Function with keyword arguments
def print_info(**kwargs):
    """Print information using keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
print_info(animal="dog", breed="golden retriever", age=3)

# Lambda functions - Small anonymous functions
print("\n=== LAMBDA FUNCTIONS ===")

# Traditional function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(f"Square of 5: {square(5)}")
print(f"Square of 5 (lambda): {square_lambda(5)}")

# Lambda with multiple parameters
add_lambda = lambda a, b: a + b
print(f"Add 3 and 4: {add_lambda(3, 4)}")

# Lambda in list operations
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# CLASSES - Object-Oriented Programming
print("\n=== CLASSES ===")

# Basic class definition
class Dog:
    """A simple Dog class"""
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor - called when creating a new instance"""
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        self.tricks = []  # Instance attribute
    
    def bark(self):
        """Method to make the dog bark"""
        return f"{self.name} says: Woof!"
    
    def add_trick(self, trick):
        """Method to add a trick to the dog's repertoire"""
        self.tricks.append(trick)
    
    def get_info(self):
        """Method to get dog information"""
        return f"{self.name} is {self.age} years old and knows {len(self.tricks)} tricks"

# Creating instances (objects) of the class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")
print(dog1.bark())
print(dog2.bark())

# Adding tricks
dog1.add_trick("sit")
dog1.add_trick("roll over")
dog2.add_trick("fetch")

print(f"After adding tricks:")
print(f"Dog 1: {dog1.get_info()}")
print(f"Dog 2: {dog2.get_info()}")

# Accessing attributes
print(f"Dog1's name: {dog1.name}")
print(f"Dog1's age: {dog1.age}")
print(f"Dog species: {Dog.species}")  # Class attribute

# INHERITANCE - Creating new classes based on existing ones
print("\n=== INHERITANCE ===")

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} makes a sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):  # Cat inherits from Animal
    """Cat class that inherits from Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "Felis catus")  # Call parent constructor
        self.breed = breed
    
    def make_sound(self):  # Override parent method
        return f"{self.name} says: Meow!"
    
    def purr(self):  # New method specific to cats
        return f"{self.name} is purring"

# Using inheritance
cat = Cat("Whiskers", "Persian")
print(cat.get_info())  # Inherited method
print(cat.make_sound())  # Overridden method
print(cat.purr())  # New method

# PROPERTIES AND ENCAPSULATION
print("\n=== PROPERTIES ===")

class BankAccount:
    """Bank account with encapsulated balance"""
    
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Private attribute (convention: underscore)
    
    @property  # Getter property
    def balance(self):
        """Get the current balance"""
        return self._balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Using the bank account
account = BankAccount(100)
print(f"Initial balance: {account.balance}")

account.deposit(50)
print(f"After depositing $50: {account.balance}")

success = account.withdraw(30)
print(f"Withdrawal successful: {success}, Balance: {account.balance}")

success = account.withdraw(200)  # Try to withdraw more than available
print(f"Withdrawal successful: {success}, Balance: {account.balance}")

# STATIC METHODS AND CLASS METHODS
print("\n=== STATIC AND CLASS METHODS ===")

class MathUtils:
    """Utility class with static and class methods"""
    
    # Class attribute
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        """Static method - doesn't need class or instance"""
        return a + b
    
    @classmethod
    def get_pi(cls):
        """Class method - receives the class as first parameter"""
        return cls.pi
    
    @classmethod
    def create_circle_area_function(cls):
        """Class method that returns a function"""
        def circle_area(radius):
            return cls.pi * radius ** 2
        return circle_area

# Using static and class methods
print(f"Static method: {MathUtils.add(5, 3)}")
print(f"Class method: {MathUtils.get_pi()}")

# Get a function from a class method
area_function = MathUtils.create_circle_area_function()
print(f"Circle area (radius=5): {area_function(5)}")
