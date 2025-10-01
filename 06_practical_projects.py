# ===========================================
# PRACTICAL PROJECTS - Real-World Examples
# ===========================================

import random
import time
import json
from datetime import datetime

# PROJECT 1: NUMBER GUESSING GAME
print("=== PROJECT 1: NUMBER GUESSING GAME ===")

def number_guessing_game():
    """A simple number guessing game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid attempts
    
    print(f"Game over! The secret number was {secret_number}.")

# Uncomment to play the game:
# number_guessing_game()

# PROJECT 2: TODO LIST MANAGER
print("\n=== PROJECT 2: TODO LIST MANAGER ===")

class TodoList:
    """A simple todo list manager"""
    
    def __init__(self):
        self.todos = []
        self.load_todos()
    
    def add_todo(self, task, priority="medium"):
        """Add a new todo item"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(todo)
        print(f"Added: {task}")
        self.save_todos()
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                print(f"Completed: {todo['task']}")
                self.save_todos()
                return
        print(f"Todo with ID {todo_id} not found!")
    
    def display_todos(self):
        """Display all todos"""
        if not self.todos:
            print("No todos found!")
            return
        
        print("\nYour Todo List:")
        print("-" * 50)
        for todo in self.todos:
            status = "✓" if todo["completed"] else "○"
            priority_color = {
                "high": "🔴",
                "medium": "🟡", 
                "low": "🟢"
            }.get(todo["priority"], "⚪")
            
            print(f"{status} {priority_color} [{todo['id']}] {todo['task']}")
            print(f"   Created: {todo['created_at']}")
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open("todos.json", "w") as file:
            json.dump(self.todos, file, indent=2)
    
    def load_todos(self):
        """Load todos from JSON file"""
        try:
            with open("todos.json", "r") as file:
                self.todos = json.load(file)
        except FileNotFoundError:
            self.todos = []

# Demo the todo list
todo_manager = TodoList()
todo_manager.add_todo("Learn Python basics", "high")
todo_manager.add_todo("Practice coding daily", "high")
todo_manager.add_todo("Read programming books", "medium")
todo_manager.add_todo("Organize workspace", "low")

todo_manager.display_todos()
todo_manager.complete_todo(1)
todo_manager.display_todos()

# PROJECT 3: CALCULATOR WITH HISTORY
print("\n=== PROJECT 3: CALCULATOR WITH HISTORY ===")

class Calculator:
    """A calculator that remembers calculation history"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers"""
        result = a + b
        self._record_calculation(f"{a} + {b}", result)
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers"""
        result = a - b
        self._record_calculation(f"{a} - {b}", result)
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        result = a * b
        self._record_calculation(f"{a} * {b}", result)
        return result
    
    def divide(self, a, b):
        """Divide two numbers"""
        if b == 0:
            print("Error: Cannot divide by zero!")
            return None
        result = a / b
        self._record_calculation(f"{a} / {b}", result)
        return result
    
    def power(self, a, b):
        """Raise a to the power of b"""
        result = a ** b
        self._record_calculation(f"{a} ^ {b}", result)
        return result
    
    def _record_calculation(self, expression, result):
        """Record a calculation in history"""
        calculation = {
            "expression": expression,
            "result": result,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.history.append(calculation)
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations in history.")
            return
        
        print("\nCalculation History:")
        print("-" * 30)
        for i, calc in enumerate(self.history[-10:], 1):  # Show last 10 calculations
            print(f"{i}. {calc['expression']} = {calc['result']} ({calc['timestamp']})")
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        print("History cleared!")

# Demo the calculator
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 * 7 = {calc.multiply(6, 7)}")
print(f"15 / 3 = {calc.divide(15, 3)}")
print(f"2 ^ 8 = {calc.power(2, 8)}")

calc.show_history()

# PROJECT 4: STUDENT GRADE MANAGER
print("\n=== PROJECT 4: STUDENT GRADE MANAGER ===")

class Student:
    """Represents a student with grades"""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, grade):
        """Add a grade for a subject"""
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
        print(f"Added grade {grade} for {subject}")
    
    def get_average(self, subject=None):
        """Calculate average grade for a subject or overall"""
        if subject:
            if subject in self.grades:
                return sum(self.grades[subject]) / len(self.grades[subject])
            return 0
        
        # Calculate overall average
        all_grades = []
        for subject_grades in self.grades.values():
            all_grades.extend(subject_grades)
        
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def get_report(self):
        """Generate a grade report"""
        report = f"\nGrade Report for {self.name} (ID: {self.student_id})"
        report += "\n" + "=" * 40
        
        for subject, grades in self.grades.items():
            avg = sum(grades) / len(grades)
            report += f"\n{subject}: {grades} (Average: {avg:.1f})"
        
        overall_avg = self.get_average()
        report += f"\n\nOverall Average: {overall_avg:.1f}"
        
        return report

class GradeManager:
    """Manages multiple students and their grades"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, student_id):
        """Add a new student"""
        self.students[student_id] = Student(name, student_id)
        print(f"Added student: {name}")
    
    def add_grade(self, student_id, subject, grade):
        """Add a grade for a specific student"""
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
        else:
            print(f"Student with ID {student_id} not found!")
    
    def get_student_report(self, student_id):
        """Get report for a specific student"""
        if student_id in self.students:
            return self.students[student_id].get_report()
        return f"Student with ID {student_id} not found!"
    
    def get_class_average(self, subject):
        """Calculate class average for a subject"""
        grades = []
        for student in self.students.values():
            if subject in student.grades:
                grades.extend(student.grades[subject])
        
        return sum(grades) / len(grades) if grades else 0

# Demo the grade manager
grade_manager = GradeManager()

# Add students
grade_manager.add_student("Alice Johnson", "S001")
grade_manager.add_student("Bob Smith", "S002")
grade_manager.add_student("Charlie Brown", "S003")

# Add grades
grade_manager.add_grade("S001", "Math", 85)
grade_manager.add_grade("S001", "Math", 90)
grade_manager.add_grade("S001", "Science", 78)
grade_manager.add_grade("S001", "English", 92)

grade_manager.add_grade("S002", "Math", 88)
grade_manager.add_grade("S002", "Science", 94)
grade_manager.add_grade("S002", "English", 87)

grade_manager.add_grade("S003", "Math", 76)
grade_manager.add_grade("S003", "Science", 82)
grade_manager.add_grade("S003", "English", 89)

# Display reports
print(grade_manager.get_student_report("S001"))
print(f"\nClass average in Math: {grade_manager.get_class_average('Math'):.1f}")

# PROJECT 5: PASSWORD GENERATOR
print("\n=== PROJECT 5: PASSWORD GENERATOR ===")

class PasswordGenerator:
    """Generate secure passwords with customizable options"""
    
    def __init__(self):
        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate_password(self, length=12, include_uppercase=True, include_digits=True, include_symbols=True):
        """Generate a random password with specified criteria"""
        characters = self.lowercase
        
        if include_uppercase:
            characters += self.uppercase
        if include_digits:
            characters += self.digits
        if include_symbols:
            characters += self.symbols
        
        # Ensure at least one character from each required type
        password = []
        if include_uppercase:
            password.append(random.choice(self.uppercase))
        if include_digits:
            password.append(random.choice(self.digits))
        if include_symbols:
            password.append(random.choice(self.symbols))
        
        # Fill the rest randomly
        for _ in range(length - len(password)):
            password.append(random.choice(characters))
        
        # Shuffle the password
        random.shuffle(password)
        return "".join(password)
    
    def check_password_strength(self, password):
        """Check the strength of a password"""
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Password should contain lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Password should contain uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Password should contain numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Password should contain special characters")
        
        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
        strength = strength_levels[min(score, len(strength_levels) - 1)]
        
        return {
            "score": score,
            "strength": strength,
            "feedback": feedback
        }

# Demo the password generator
pw_gen = PasswordGenerator()

print("Generated passwords:")
for i in range(3):
    password = pw_gen.generate_password(length=12)
    strength = pw_gen.check_password_strength(password)
    print(f"{i+1}. {password} (Strength: {strength['strength']})")

# Test password strength
test_password = "MyPassword123!"
strength_result = pw_gen.check_password_strength(test_password)
print(f"\nPassword: {test_password}")
print(f"Strength: {strength_result['strength']} (Score: {strength_result['score']}/5)")

if strength_result['feedback']:
    print("Suggestions:")
    for suggestion in strength_result['feedback']:
        print(f"  - {suggestion}")

print("\n=== All projects completed! ===")
print("These examples demonstrate practical Python programming concepts.")
print("Try running each project and modifying them to learn more!")
