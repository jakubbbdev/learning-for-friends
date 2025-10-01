# ===========================================
# DATA STRUCTURES - Organizing and Storing Data
# ===========================================

# LISTS - Ordered collection of items (can be modified)
print("=== LISTS ===")

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]  # Lists can contain different data types
empty_list = []  # Empty list

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed: {mixed}")

# Accessing list elements (indexing starts at 0)
print(f"First fruit: {fruits[0]}")  # apple
print(f"Second fruit: {fruits[1]}")  # banana
print(f"Last fruit: {fruits[-1]}")  # orange (negative index counts from end)

# List slicing [start:end:step]
print(f"First two fruits: {fruits[0:2]}")  # ['apple', 'banana']
print(f"All fruits: {fruits[:]}")  # ['apple', 'banana', 'orange']
print(f"Last two fruits: {fruits[-2:]}")  # ['banana', 'orange']

# Modifying lists
fruits.append("grape")  # Add item to end
print(f"After adding grape: {fruits}")

fruits.insert(1, "mango")  # Insert at specific position
print(f"After inserting mango at position 1: {fruits}")

fruits.remove("banana")  # Remove specific item
print(f"After removing banana: {fruits}")

popped_item = fruits.pop()  # Remove and return last item
print(f"Popped item: {popped_item}")
print(f"Fruits after pop: {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sorted: {sorted(numbers)}")  # Doesn't modify original
numbers.sort()  # Modifies the original list
print(f"After sort(): {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# TUPLES - Ordered collection that cannot be modified (immutable)
print("\n=== TUPLES ===")

coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single-item tuple

print(f"Coordinates: {coordinates}")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")

# You cannot modify tuples
# coordinates[0] = 15  # This would cause an error!

# DICTIONARIES - Key-value pairs (like a real dictionary)
print("\n=== DICTIONARIES ===")

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

grades = {
    "math": 95,
    "science": 87,
    "english": 92
}

print(f"Person: {person}")
print(f"Grades: {grades}")

# Accessing dictionary values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Math grade: {grades['math']}")

# Safe access with get() method
print(f"Physics grade: {grades.get('physics', 'Not taken')}")  # Returns default if key doesn't exist

# Modifying dictionaries
person["age"] = 31  # Update existing key
person["email"] = "alice@email.com"  # Add new key-value pair
print(f"Updated person: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# SETS - Unordered collection of unique items
print("\n=== SETS ===")

# Creating sets
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange", "apple"}  # Duplicates are automatically removed
print(f"Numbers set: {numbers_set}")
print(f"Fruits set: {fruits_set}")  # Only one "apple"

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")  # All unique elements from both sets
print(f"Intersection: {set1 & set2}")  # Elements in both sets
print(f"Difference: {set1 - set2}")  # Elements in set1 but not in set2
print(f"Symmetric difference: {set1 ^ set2}")  # Elements in either set but not both

# Adding and removing from sets
fruits_set.add("grape")
fruits_set.remove("banana")  # Raises error if item doesn't exist
fruits_set.discard("kiwi")  # Doesn't raise error if item doesn't exist
print(f"Updated fruits set: {fruits_set}")

# LIST COMPREHENSIONS - Creating lists in a concise way
print("\n=== LIST COMPREHENSIONS ===")

# Traditional way
squares_traditional = []
for i in range(1, 6):
    squares_traditional.append(i ** 2)
print(f"Squares (traditional): {squares_traditional}")

# List comprehension way
squares_comprehension = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comprehension}")

# List comprehension with condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(f"Word lengths: {word_lengths}")

# PRACTICAL EXAMPLE - Student grades
print("\n=== PRACTICAL EXAMPLE ===")

students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 94]},
    {"name": "Charlie", "grades": [76, 82, 80]}
]

# Calculate average grades for each student
for student in students:
    average = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: {average:.1f}")  # .1f means 1 decimal place

# Find students with average above 85
top_students = [s["name"] for s in students if sum(s["grades"]) / len(s["grades"]) > 85]
print(f"Top students: {top_students}")
