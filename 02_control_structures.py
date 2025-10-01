# ===========================================
# CONTROL STRUCTURES - Making Decisions and Repeating Code
# ===========================================

# IF STATEMENTS - Making decisions based on conditions
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:  # elif = "else if" - check another condition
    print("You are a teenager")
else:  # if none of the above conditions are true
    print("You are a child")

# Multiple conditions
score = 85
attendance = 90

if score >= 80 and attendance >= 80:  # Both conditions must be true
    print("Excellent student!")
elif score >= 60 or attendance >= 70:  # At least one condition must be true
    print("Good student")
else:
    print("Needs improvement")

# Comparison operators
x = 10
y = 5

print(f"x == y: {x == y}")  # Equal to (False)
print(f"x != y: {x != y}")  # Not equal to (True)
print(f"x > y: {x > y}")    # Greater than (True)
print(f"x < y: {x < y}")    # Less than (False)
print(f"x >= y: {x >= y}")  # Greater than or equal to (True)
print(f"x <= y: {x <= y}")  # Less than or equal to (False)

# FOR LOOPS - Repeating code a specific number of times
print("\n--- For Loop Examples ---")

# Loop through a range of numbers
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Count: {i}")

# Loop through a range with start and end
for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(f"Number: {i}")

# Loop through a range with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"Even number: {i}")

# Loop through a list
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with index and value
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# WHILE LOOPS - Repeating code while a condition is true
print("\n--- While Loop Examples ---")

# Countdown example
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # Decrease count by 1
print("Blast off!")

# User input validation
valid_input = False
while not valid_input:
    user_age = input("Enter your age (must be a number): ")
    if user_age.isdigit():  # Check if input contains only digits
        age = int(user_age)
        print(f"You are {age} years old")
        valid_input = True
    else:
        print("Please enter a valid number!")

# BREAK and CONTINUE - Control loop execution
print("\n--- Break and Continue Examples ---")

# Break - exit the loop completely
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(f"Number: {i}")

print("Loop ended with break")

# Continue - skip to the next iteration
for i in range(10):
    if i % 2 == 0:  # If i is even
        continue  # Skip the rest of this iteration
    print(f"Odd number: {i}")

# NESTED LOOPS - Loops inside other loops
print("\n--- Nested Loop Example ---")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")

# This will print:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
