# ===========================================
# ADVANCED PROJECTS - Real-World Applications
# ===========================================

print("=== ADVANCED PYTHON PROJECTS ===")

import json
import sqlite3
import random
import hashlib
import os
from datetime import datetime, timedelta
from collections import defaultdict

# PROJECT 1: COMPREHENSIVE CONTACT MANAGEMENT SYSTEM
print("\n=== PROJECT 1: CONTACT MANAGEMENT SYSTEM ===")

class Contact:
    """Represents a contact with all necessary information"""
    
    def __init__(self, name, phone, email, address="", notes=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.notes = notes
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert contact to dictionary"""
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create contact from dictionary"""
        contact = cls(
            data['name'],
            data['phone'],
            data['email'],
            data.get('address', ''),
            data.get('notes', '')
        )
        contact.created_at = datetime.fromisoformat(data['created_at'])
        contact.updated_at = datetime.fromisoformat(data['updated_at'])
        return contact
    
    def update(self, **kwargs):
        """Update contact fields"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()
    
    def __str__(self):
        return f"Contact(name='{self.name}', phone='{self.phone}', email='{self.email}')"

class ContactManager:
    """Manages a collection of contacts with database persistence"""
    
    def __init__(self, db_name="contacts.db"):
        self.db_name = db_name
        self.contacts = {}
        self.setup_database()
        self.load_contacts()
    
    def setup_database(self):
        """Set up SQLite database for contacts"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT,
                notes TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_contact(self, contact):
        """Add a new contact"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO contacts (name, phone, email, address, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            contact.name, contact.phone, contact.email, contact.address,
            contact.notes, contact.created_at, contact.updated_at
        ))
        
        contact_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        self.contacts[contact_id] = contact
        return contact_id
    
    def get_contact(self, contact_id):
        """Get contact by ID"""
        return self.contacts.get(contact_id)
    
    def search_contacts(self, query):
        """Search contacts by name, phone, or email"""
        results = []
        query_lower = query.lower()
        
        for contact_id, contact in self.contacts.items():
            if (query_lower in contact.name.lower() or
                query_lower in contact.phone or
                query_lower in contact.email.lower()):
                results.append((contact_id, contact))
        
        return results
    
    def update_contact(self, contact_id, **kwargs):
        """Update contact information"""
        contact = self.contacts.get(contact_id)
        if not contact:
            return False
        
        contact.update(**kwargs)
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE contacts SET name=?, phone=?, email=?, address=?, notes=?, updated_at=?
            WHERE id=?
        """, (
            contact.name, contact.phone, contact.email, contact.address,
            contact.notes, contact.updated_at, contact_id
        ))
        
        conn.commit()
        conn.close()
        return True
    
    def delete_contact(self, contact_id):
        """Delete a contact"""
        if contact_id not in self.contacts:
            return False
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        conn.close()
        
        del self.contacts[contact_id]
        return True
    
    def load_contacts(self):
        """Load contacts from database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        
        for row in rows:
            contact_id, name, phone, email, address, notes, created_at, updated_at = row
            contact = Contact(name, phone, email, address, notes)
            contact.created_at = datetime.fromisoformat(created_at)
            contact.updated_at = datetime.fromisoformat(updated_at)
            self.contacts[contact_id] = contact
        
        conn.close()
    
    def export_contacts(self, filename):
        """Export contacts to JSON file"""
        contacts_data = {}
        for contact_id, contact in self.contacts.items():
            contacts_data[str(contact_id)] = contact.to_dict()
        
        with open(filename, 'w') as file:
            json.dump(contacts_data, file, indent=2)
        
        print(f"Exported {len(self.contacts)} contacts to {filename}")
    
    def import_contacts(self, filename):
        """Import contacts from JSON file"""
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
            
            imported_count = 0
            for contact_id, contact_data in contacts_data.items():
                contact = Contact.from_dict(contact_data)
                self.add_contact(contact)
                imported_count += 1
            
            print(f"Imported {imported_count} contacts from {filename}")
            
        except FileNotFoundError:
            print(f"File {filename} not found")
        except json.JSONDecodeError:
            print(f"Invalid JSON in {filename}")
    
    def get_statistics(self):
        """Get contact statistics"""
        total_contacts = len(self.contacts)
        
        # Count contacts by domain
        domains = defaultdict(int)
        for contact in self.contacts.values():
            domain = contact.email.split('@')[1] if '@' in contact.email else 'unknown'
            domains[domain] += 1
        
        return {
            'total_contacts': total_contacts,
            'domains': dict(domains),
            'oldest_contact': min((c.created_at for c in self.contacts.values()), default=None),
            'newest_contact': max((c.created_at for c in self.contacts.values()), default=None)
        }

# Demo the contact management system
print("\n--- Contact Management System Demo ---")

contact_manager = ContactManager()

# Add sample contacts
contacts_to_add = [
    Contact("Alice Johnson", "555-1234", "alice@email.com", "123 Main St", "Friend from college"),
    Contact("Bob Smith", "555-5678", "bob@company.com", "456 Oak Ave", "Work colleague"),
    Contact("Charlie Brown", "555-9012", "charlie@gmail.com", "", "Neighbor"),
    Contact("Diana Prince", "555-3456", "diana@superhero.com", "789 Hero St", "Superhero friend")
]

for contact in contacts_to_add:
    contact_manager.add_contact(contact)

print(f"Added {len(contacts_to_add)} contacts")

# Search contacts
search_results = contact_manager.search_contacts("alice")
print(f"\nSearch for 'alice': {len(search_results)} results")
for contact_id, contact in search_results:
    print(f"  {contact}")

# Get statistics
stats = contact_manager.get_statistics()
print(f"\nContact Statistics:")
print(f"  Total contacts: {stats['total_contacts']}")
print(f"  Email domains: {stats['domains']}")

# Export contacts
contact_manager.export_contacts("contacts_backup.json")

# PROJECT 2: EXPENSE TRACKER
print("\n=== PROJECT 2: EXPENSE TRACKER ===")

class Expense:
    """Represents a single expense"""
    
    def __init__(self, amount, description, category, date=None):
        self.amount = float(amount)
        self.description = description
        self.category = category
        self.date = date or datetime.now()
        self.id = None
    
    def to_dict(self):
        """Convert expense to dictionary"""
        return {
            'amount': self.amount,
            'description': self.description,
            'category': self.category,
            'date': self.date.isoformat(),
            'id': self.id
        }

class ExpenseTracker:
    """Tracks and analyzes expenses"""
    
    def __init__(self, db_name="expenses.db"):
        self.db_name = db_name
        self.expenses = []
        self.categories = set()
        self.setup_database()
        self.load_expenses()
    
    def setup_database(self):
        """Set up database for expenses"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                description TEXT NOT NULL,
                category TEXT NOT NULL,
                date TIMESTAMP NOT NULL
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_expense(self, expense):
        """Add a new expense"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO expenses (amount, description, category, date)
            VALUES (?, ?, ?, ?)
        """, (expense.amount, expense.description, expense.category, expense.date))
        
        expense.id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        self.expenses.append(expense)
        self.categories.add(expense.category)
    
    def load_expenses(self):
        """Load expenses from database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
        rows = cursor.fetchall()
        
        for row in rows:
            expense_id, amount, description, category, date = row
            expense = Expense(amount, description, category, datetime.fromisoformat(date))
            expense.id = expense_id
            self.expenses.append(expense)
            self.categories.add(category)
        
        conn.close()
    
    def get_expenses_by_category(self, category):
        """Get all expenses in a category"""
        return [exp for exp in self.expenses if exp.category == category]
    
    def get_expenses_by_date_range(self, start_date, end_date):
        """Get expenses within a date range"""
        return [exp for exp in self.expenses if start_date <= exp.date <= end_date]
    
    def get_monthly_summary(self, year, month):
        """Get summary for a specific month"""
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        
        monthly_expenses = self.get_expenses_by_date_range(start_date, end_date)
        
        total_amount = sum(exp.amount for exp in monthly_expenses)
        category_totals = defaultdict(float)
        
        for expense in monthly_expenses:
            category_totals[expense.category] += expense.amount
        
        return {
            'total_amount': total_amount,
            'expense_count': len(monthly_expenses),
            'category_totals': dict(category_totals),
            'average_expense': total_amount / len(monthly_expenses) if monthly_expenses else 0
        }
    
    def get_category_analysis(self):
        """Analyze expenses by category"""
        category_stats = defaultdict(lambda: {'total': 0, 'count': 0, 'avg': 0})
        
        for expense in self.expenses:
            category_stats[expense.category]['total'] += expense.amount
            category_stats[expense.category]['count'] += 1
        
        # Calculate averages
        for category, stats in category_stats.items():
            stats['avg'] = stats['total'] / stats['count']
        
        return dict(category_stats)
    
    def generate_report(self, start_date=None, end_date=None):
        """Generate a comprehensive expense report"""
        if not start_date:
            start_date = min((exp.date for exp in self.expenses), default=datetime.now())
        if not end_date:
            end_date = max((exp.date for exp in self.expenses), default=datetime.now())
        
        period_expenses = self.get_expenses_by_date_range(start_date, end_date)
        
        if not period_expenses:
            return "No expenses found for the specified period."
        
        total_amount = sum(exp.amount for exp in period_expenses)
        category_analysis = self.get_category_analysis()
        
        report = f"""
EXPENSE REPORT
==============
Period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}
Total Expenses: ${total_amount:.2f}
Number of Transactions: {len(period_expenses)}
Average per Transaction: ${total_amount/len(period_expenses):.2f}

TOP CATEGORIES:
"""
        
        sorted_categories = sorted(category_analysis.items(), 
                                 key=lambda x: x[1]['total'], reverse=True)
        
        for category, stats in sorted_categories[:5]:
            percentage = (stats['total'] / total_amount) * 100
            report += f"  {category}: ${stats['total']:.2f} ({percentage:.1f}%)\n"
        
        return report

# Demo the expense tracker
print("\n--- Expense Tracker Demo ---")

expense_tracker = ExpenseTracker()

# Add sample expenses
sample_expenses = [
    Expense(15.99, "Lunch at restaurant", "Food", datetime.now() - timedelta(days=1)),
    Expense(45.50, "Gas station", "Transportation", datetime.now() - timedelta(days=2)),
    Expense(120.00, "Grocery shopping", "Food", datetime.now() - timedelta(days=3)),
    Expense(25.00, "Movie tickets", "Entertainment", datetime.now() - timedelta(days=4)),
    Expense(89.99, "Online shopping", "Shopping", datetime.now() - timedelta(days=5)),
    Expense(12.50, "Coffee", "Food", datetime.now() - timedelta(days=6)),
    Expense(200.00, "Electric bill", "Utilities", datetime.now() - timedelta(days=7))
]

for expense in sample_expenses:
    expense_tracker.add_expense(expense)

print(f"Added {len(sample_expenses)} expenses")

# Generate report
current_month = datetime.now()
report = expense_tracker.generate_report()
print(report)

# PROJECT 3: PASSWORD MANAGER
print("\n=== PROJECT 3: PASSWORD MANAGER ===")

class PasswordManager:
    """Secure password manager with encryption"""
    
    def __init__(self, master_password, db_name="passwords.db"):
        self.master_password = master_password
        self.db_name = db_name
        self.passwords = {}
        self.setup_database()
        self.load_passwords()
    
    def setup_database(self):
        """Set up encrypted password database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT,
                encrypted_password TEXT NOT NULL,
                website TEXT,
                notes TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _encrypt_password(self, password):
        """Simple encryption (in real app, use proper encryption)"""
        # This is a simple example - use proper encryption in production
        key = hashlib.sha256(self.master_password.encode()).digest()
        encrypted = hashlib.pbkdf2_hmac('sha256', password.encode(), key, 100000)
        return encrypted.hex()
    
    def _decrypt_password(self, encrypted_password):
        """Simple decryption (in real app, use proper decryption)"""
        # This is a simplified example
        # In production, you'd implement proper decryption
        return "decrypted_password"  # Placeholder
    
    def add_password(self, service, username, password, website="", notes=""):
        """Add a new password entry"""
        encrypted_password = self._encrypt_password(password)
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO passwords (service, username, encrypted_password, website, notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (service, username, encrypted_password, website, notes, 
              datetime.now(), datetime.now()))
        
        password_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Store in memory (without actual password for security)
        self.passwords[password_id] = {
            'service': service,
            'username': username,
            'website': website,
            'notes': notes,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        
        return password_id
    
    def get_password_info(self, password_id):
        """Get password information (without actual password)"""
        return self.passwords.get(password_id)
    
    def search_passwords(self, query):
        """Search passwords by service or username"""
        results = []
        query_lower = query.lower()
        
        for password_id, info in self.passwords.items():
            if (query_lower in info['service'].lower() or
                query_lower in info['username'].lower()):
                results.append((password_id, info))
        
        return results
    
    def load_passwords(self):
        """Load passwords from database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, service, username, website, notes, created_at, updated_at FROM passwords")
        rows = cursor.fetchall()
        
        for row in rows:
            password_id, service, username, website, notes, created_at, updated_at = row
            self.passwords[password_id] = {
                'service': service,
                'username': username,
                'website': website,
                'notes': notes,
                'created_at': datetime.fromisoformat(created_at),
                'updated_at': datetime.fromisoformat(updated_at)
            }
        
        conn.close()
    
    def generate_secure_password(self, length=12, include_symbols=True):
        """Generate a secure random password"""
        import string
        import secrets
        
        characters = string.ascii_letters + string.digits
        if include_symbols:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    def get_statistics(self):
        """Get password manager statistics"""
        return {
            'total_passwords': len(self.passwords),
            'services': list(set(info['service'] for info in self.passwords.values())),
            'oldest_password': min((info['created_at'] for info in self.passwords.values()), default=None),
            'newest_password': max((info['created_at'] for info in self.passwords.values()), default=None)
        }

# Demo the password manager
print("\n--- Password Manager Demo ---")

password_manager = PasswordManager("master_password_123")

# Add sample passwords
password_manager.add_password("Gmail", "user@gmail.com", "secure_password_123", "gmail.com", "Personal email")
password_manager.add_password("GitHub", "developer", "github_password_456", "github.com", "Code repository")
password_manager.add_password("Bank", "account_holder", "bank_password_789", "mybank.com", "Online banking")

print(f"Added {len(password_manager.passwords)} password entries")

# Search passwords
search_results = password_manager.search_passwords("gmail")
print(f"\nSearch results for 'gmail':")
for password_id, info in search_results:
    print(f"  {info['service']} - {info['username']} ({info['website']})")

# Generate secure password
secure_password = password_manager.generate_secure_password(16, True)
print(f"\nGenerated secure password: {secure_password}")

# Get statistics
stats = password_manager.get_statistics()
print(f"\nPassword Manager Statistics:")
print(f"  Total passwords: {stats['total_passwords']}")
print(f"  Services: {', '.join(stats['services'])}")

# PROJECT 4: TASK MANAGEMENT SYSTEM
print("\n=== PROJECT 4: TASK MANAGEMENT SYSTEM ===")

class Task:
    """Represents a single task"""
    
    def __init__(self, title, description="", priority="medium", due_date=None):
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high
        self.status = "pending"  # pending, in_progress, completed, cancelled
        self.due_date = due_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = None
    
    def update_status(self, new_status):
        """Update task status"""
        valid_statuses = ["pending", "in_progress", "completed", "cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
            self.updated_at = datetime.now()
            return True
        return False
    
    def is_overdue(self):
        """Check if task is overdue"""
        if self.due_date and self.status not in ["completed", "cancelled"]:
            return datetime.now() > self.due_date
        return False

class TaskManager:
    """Manages tasks with priority and due date handling"""
    
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.tasks = {}
        self.setup_database()
        self.load_tasks()
    
    def setup_database(self):
        """Set up task database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                due_date TIMESTAMP,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_task(self, task):
        """Add a new task"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO tasks (title, description, priority, status, due_date, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (task.title, task.description, task.priority, task.status, 
              task.due_date, task.created_at, task.updated_at))
        
        task.id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        self.tasks[task.id] = task
        return task.id
    
    def load_tasks(self):
        """Load tasks from database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        
        for row in rows:
            task_id, title, description, priority, status, due_date, created_at, updated_at = row
            task = Task(title, description, priority, 
                       datetime.fromisoformat(due_date) if due_date else None)
            task.status = status
            task.id = task_id
            task.created_at = datetime.fromisoformat(created_at)
            task.updated_at = datetime.fromisoformat(updated_at)
            self.tasks[task_id] = task
        
        conn.close()
    
    def get_tasks_by_status(self, status):
        """Get tasks by status"""
        return [task for task in self.tasks.values() if task.status == status]
    
    def get_tasks_by_priority(self, priority):
        """Get tasks by priority"""
        return [task for task in self.tasks.values() if task.priority == priority]
    
    def get_overdue_tasks(self):
        """Get all overdue tasks"""
        return [task for task in self.tasks.values() if task.is_overdue()]
    
    def get_tasks_due_soon(self, days=7):
        """Get tasks due within specified days"""
        cutoff_date = datetime.now() + timedelta(days=days)
        return [task for task in self.tasks.values() 
                if task.due_date and task.due_date <= cutoff_date and task.status not in ["completed", "cancelled"]]
    
    def get_dashboard_data(self):
        """Get data for task dashboard"""
        total_tasks = len(self.tasks)
        pending_tasks = len(self.get_tasks_by_status("pending"))
        in_progress_tasks = len(self.get_tasks_by_status("in_progress"))
        completed_tasks = len(self.get_tasks_by_status("completed"))
        overdue_tasks = len(self.get_overdue_tasks())
        due_soon = len(self.get_tasks_due_soon())
        
        return {
            'total_tasks': total_tasks,
            'pending_tasks': pending_tasks,
            'in_progress_tasks': in_progress_tasks,
            'completed_tasks': completed_tasks,
            'overdue_tasks': overdue_tasks,
            'due_soon': due_soon,
            'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }
    
    def generate_report(self):
        """Generate task management report"""
        dashboard = self.get_dashboard_data()
        
        report = f"""
TASK MANAGEMENT REPORT
======================
Total Tasks: {dashboard['total_tasks']}
Pending: {dashboard['pending_tasks']}
In Progress: {dashboard['in_progress_tasks']}
Completed: {dashboard['completed_tasks']}
Overdue: {dashboard['overdue_tasks']}
Due Soon (7 days): {dashboard['due_soon']}
Completion Rate: {dashboard['completion_rate']:.1f}%

PRIORITY BREAKDOWN:
"""
        
        priority_counts = defaultdict(int)
        for task in self.tasks.values():
            priority_counts[task.priority] += 1
        
        for priority in ["high", "medium", "low"]:
            count = priority_counts[priority]
            percentage = (count / dashboard['total_tasks'] * 100) if dashboard['total_tasks'] > 0 else 0
            report += f"  {priority.capitalize()}: {count} ({percentage:.1f}%)\n"
        
        return report

# Demo the task management system
print("\n--- Task Management System Demo ---")

task_manager = TaskManager()

# Add sample tasks
sample_tasks = [
    Task("Learn Python basics", "Complete Python tutorial", "high", datetime.now() + timedelta(days=3)),
    Task("Buy groceries", "Milk, bread, eggs", "medium", datetime.now() + timedelta(days=1)),
    Task("Finish project report", "Write final report for work", "high", datetime.now() + timedelta(days=5)),
    Task("Call dentist", "Schedule annual checkup", "low", datetime.now() + timedelta(days=14)),
    Task("Exercise", "Go to gym", "medium", datetime.now() + timedelta(days=2))
]

for task in sample_tasks:
    task_manager.add_task(task)

print(f"Added {len(sample_tasks)} tasks")

# Update some task statuses
tasks = list(task_manager.tasks.values())
tasks[0].update_status("in_progress")
tasks[4].update_status("completed")

# Generate report
report = task_manager.generate_report()
print(report)

# Get overdue tasks
overdue = task_manager.get_overdue_tasks()
if overdue:
    print(f"\nOverdue tasks ({len(overdue)}):")
    for task in overdue:
        print(f"  - {task.title} (due: {task.due_date.strftime('%Y-%m-%d')})")
else:
    print("\nNo overdue tasks!")

# BEST PRACTICES FOR ADVANCED PROJECTS
print("\n=== ADVANCED PROJECT BEST PRACTICES ===")
print("1. Use proper database design with foreign keys and indexes")
print("2. Implement proper error handling and validation")
print("3. Use encryption for sensitive data")
print("4. Implement logging for debugging and monitoring")
print("5. Create comprehensive unit tests")
print("6. Use configuration files for settings")
print("7. Implement proper backup and restore functionality")
print("8. Add user authentication and authorization")
print("9. Use environment variables for sensitive information")
print("10. Document your code with docstrings and comments")
print("11. Implement data validation and sanitization")
print("12. Use proper exception handling")
print("13. Consider scalability and performance")
print("14. Implement proper logging and monitoring")
print("15. Use version control for your projects")

print("\n=== Advanced Projects Complete ===")
print("These projects demonstrate real-world Python applications!")
print("Try extending them with additional features and functionality.")
