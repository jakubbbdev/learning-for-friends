# ===========================================
# FILE HANDLING - Reading and Writing Files
# ===========================================

import os  # For file system operations

print("=== FILE HANDLING BASICS ===")

# WRITING TO FILES
print("\n--- Writing to Files ---")

# Create some sample data
students = [
    {"name": "Alice", "grade": 85, "subject": "Math"},
    {"name": "Bob", "grade": 92, "subject": "Science"},
    {"name": "Charlie", "grade": 78, "subject": "English"}
]

# Writing to a text file
with open("students.txt", "w") as file:  # 'w' = write mode (creates new file or overwrites)
    file.write("Student Grades Report\n")
    file.write("=" * 20 + "\n")
    
    for student in students:
        file.write(f"Name: {student['name']}\n")
        file.write(f"Grade: {student['grade']}\n")
        file.write(f"Subject: {student['subject']}\n")
        file.write("-" * 15 + "\n")

print("Written to students.txt")

# Writing multiple lines at once
poem_lines = [
    "Roses are red",
    "Violets are blue", 
    "Python is awesome",
    "And so are you!"
]

with open("poem.txt", "w") as file:
    file.writelines(line + "\n" for line in poem_lines)

print("Written to poem.txt")

# READING FROM FILES
print("\n--- Reading from Files ---")

# Reading entire file content
try:
    with open("students.txt", "r") as file:  # 'r' = read mode
        content = file.read()
        print("Students file content:")
        print(content)
except FileNotFoundError:
    print("File not found!")

# Reading file line by line
try:
    with open("poem.txt", "r") as file:
        print("\nPoem (line by line):")
        for line_number, line in enumerate(file, 1):
            print(f"{line_number}: {line.strip()}")  # strip() removes newline characters
except FileNotFoundError:
    print("Poem file not found!")

# Reading all lines into a list
try:
    with open("poem.txt", "r") as file:
        lines = file.readlines()  # Returns list of lines
        print(f"\nTotal lines: {len(lines)}")
        print(f"First line: {lines[0].strip()}")
        print(f"Last line: {lines[-1].strip()}")
except FileNotFoundError:
    print("Poem file not found!")

# APPENDING TO FILES
print("\n--- Appending to Files ---")

# Append mode ('a') - adds to end of file without overwriting
with open("students.txt", "a") as file:
    file.write("\nAdditional Student:\n")
    file.write("Name: Diana\n")
    file.write("Grade: 88\n")
    file.write("Subject: History\n")

print("Appended to students.txt")

# DIFFERENT FILE MODES
print("\n--- File Modes ---")

# 'w' - Write mode (overwrites existing file)
# 'r' - Read mode (file must exist)
# 'a' - Append mode (adds to end of file)
# 'x' - Exclusive creation (fails if file exists)
# 'b' - Binary mode (for images, videos, etc.)
# 't' - Text mode (default)

# Example with binary mode (for copying files)
original_data = b"This is binary data: \x48\x65\x6c\x6c\x6f"  # "Hello" in bytes

with open("binary_file.dat", "wb") as file:  # 'wb' = write binary
    file.write(original_data)

# Read it back
with open("binary_file.dat", "rb") as file:  # 'rb' = read binary
    binary_content = file.read()
    print(f"Binary content: {binary_content}")
    print(f"Decoded: {binary_content.decode('utf-8', errors='ignore')}")

# WORKING WITH CSV FILES
print("\n--- CSV File Handling ---")

import csv  # Built-in CSV module

# Writing CSV data
csv_data = [
    ["Name", "Age", "City", "Occupation"],
    ["Alice", "25", "New York", "Engineer"],
    ["Bob", "30", "Los Angeles", "Teacher"],
    ["Charlie", "35", "Chicago", "Doctor"]
]

with open("people.csv", "w", newline="") as file:  # newline="" prevents extra blank lines
    writer = csv.writer(file)
    writer.writerows(csv_data)  # Write all rows at once

print("Written to people.csv")

# Reading CSV data
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    print("\nCSV Content:")
    for row in reader:
        print(f"Row: {row}")

# Reading CSV as dictionary
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)  # First row becomes keys
    print("\nCSV as Dictionary:")
    for row in reader:
        print(f"Person: {row}")

# WORKING WITH JSON FILES
print("\n--- JSON File Handling ---")

import json  # Built-in JSON module

# Python dictionary to save as JSON
book_data = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2023,
    "chapters": [
        {"number": 1, "title": "Introduction", "pages": 25},
        {"number": 2, "title": "Variables", "pages": 30},
        {"number": 3, "title": "Functions", "pages": 40}
    ],
    "available": True
}

# Writing JSON file
with open("book.json", "w") as file:
    json.dump(book_data, file, indent=2)  # indent=2 makes it pretty-printed

print("Written to book.json")

# Reading JSON file
with open("book.json", "r") as file:
    loaded_book = json.load(file)

print(f"\nLoaded book title: {loaded_book['title']}")
print(f"Author: {loaded_book['author']}")
print(f"Number of chapters: {len(loaded_book['chapters'])}")

# FILE SYSTEM OPERATIONS
print("\n--- File System Operations ---")

# Check if file exists
print(f"students.txt exists: {os.path.exists('students.txt')}")
print(f"nonexistent.txt exists: {os.path.exists('nonexistent.txt')}")

# Get file information
if os.path.exists("students.txt"):
    file_size = os.path.getsize("students.txt")
    print(f"students.txt size: {file_size} bytes")

# List files in current directory
print(f"\nFiles in current directory:")
for file in os.listdir("."):
    if file.endswith((".txt", ".csv", ".json", ".py", ".dat")):
        print(f"  - {file}")

# Create and remove directories
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Created test_folder directory")

# Create a file in the new directory
with open("test_folder/sample.txt", "w") as file:
    file.write("This is a test file in a subdirectory")

print("Created file in test_folder")

# Remove the test file and directory
os.remove("test_folder/sample.txt")
os.rmdir("test_folder")
print("Removed test files and directory")

# ERROR HANDLING WITH FILES
print("\n--- Error Handling ---")

def safe_read_file(filename):
    """Safely read a file with proper error handling"""
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'"
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Test the safe read function
result1 = safe_read_file("students.txt")
print(f"Reading existing file: {result1[:50]}...")

result2 = safe_read_file("nonexistent.txt")
print(f"Reading non-existent file: {result2}")

# PRACTICAL EXAMPLE - Simple Contact Manager
print("\n--- Practical Example: Contact Manager ---")

def save_contact(name, email, phone, filename="contacts.json"):
    """Save a contact to JSON file"""
    contacts = []
    
    # Load existing contacts if file exists
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contacts = json.load(file)
    
    # Add new contact
    new_contact = {
        "name": name,
        "email": email,
        "phone": phone
    }
    contacts.append(new_contact)
    
    # Save updated contacts
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=2)
    
    print(f"Contact '{name}' saved successfully")

def load_contacts(filename="contacts.json"):
    """Load all contacts from JSON file"""
    if not os.path.exists(filename):
        print("No contacts file found")
        return []
    
    with open(filename, "r") as file:
        contacts = json.load(file)
    
    return contacts

def display_contacts(filename="contacts.json"):
    """Display all contacts"""
    contacts = load_contacts(filename)
    
    if not contacts:
        print("No contacts found")
        return
    
    print(f"\nContacts ({len(contacts)} total):")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   Email: {contact['email']}")
        print(f"   Phone: {contact['phone']}")
        print()

# Test the contact manager
save_contact("Alice Johnson", "alice@email.com", "555-1234")
save_contact("Bob Smith", "bob@email.com", "555-5678")
save_contact("Charlie Brown", "charlie@email.com", "555-9012")

display_contacts()
