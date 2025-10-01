# ===========================================
# DATABASE OPERATIONS - Working with Data Storage
# ===========================================

print("=== DATABASE OPERATIONS ===")

# IMPORTANT NOTE: This tutorial covers SQLite (built into Python)
# For other databases like MySQL, PostgreSQL, you need additional drivers

# SQLITE BASICS
print("\n--- SQLite Basics ---")

import sqlite3
import json
from datetime import datetime

# SQLite is a lightweight database that stores data in a single file
# It's perfect for learning and small applications

# CREATING AND CONNECTING TO A DATABASE
print("\n--- Creating Database Connection ---")

def create_database_connection(db_name="learning_db.sqlite"):
    """Create a connection to SQLite database"""
    try:
        # Connect to database (creates file if it doesn't exist)
        connection = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Create connection
conn = create_database_connection()

# CREATING TABLES
print("\n--- Creating Tables ---")

def create_tables(connection):
    """Create sample tables in the database"""
    try:
        cursor = connection.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create posts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        # Create categories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )
        """)
        
        # Commit the changes
        connection.commit()
        print("Tables created successfully!")
        
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

# Create tables
create_tables(conn)

# INSERTING DATA
print("\n--- Inserting Data ---")

def insert_sample_data(connection):
    """Insert sample data into tables"""
    try:
        cursor = connection.cursor()
        
        # Insert users
        users_data = [
            ('alice', 'alice@email.com', 25),
            ('bob', 'bob@email.com', 30),
            ('charlie', 'charlie@email.com', 35),
            ('diana', 'diana@email.com', 28)
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO users (username, email, age) VALUES (?, ?, ?)",
            users_data
        )
        
        # Insert categories
        categories_data = [
            ('Technology', 'Posts about technology and programming'),
            ('Science', 'Scientific discoveries and research'),
            ('Travel', 'Travel experiences and tips'),
            ('Food', 'Cooking recipes and restaurant reviews')
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO categories (name, description) VALUES (?, ?)",
            categories_data
        )
        
        # Insert posts
        posts_data = [
            (1, 'Learning Python', 'Python is an amazing programming language for beginners.'),
            (1, 'Web Scraping Tips', 'Here are some best practices for web scraping.'),
            (2, 'Database Design', 'Understanding how to design efficient databases.'),
            (3, 'Traveling to Japan', 'My amazing experience visiting Tokyo and Kyoto.'),
            (2, 'Machine Learning Basics', 'Introduction to machine learning concepts.'),
            (4, 'Homemade Pizza Recipe', 'How to make delicious pizza at home.')
        ]
        
        cursor.executemany(
            "INSERT OR IGNORE INTO posts (user_id, title, content) VALUES (?, ?, ?)",
            posts_data
        )
        
        # Commit changes
        connection.commit()
        print("Sample data inserted successfully!")
        
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

# Insert sample data
insert_sample_data(conn)

# QUERYING DATA
print("\n--- Querying Data ---")

def query_data_examples(connection):
    """Demonstrate various SQL queries"""
    try:
        cursor = connection.cursor()
        
        # Basic SELECT query
        print("\n1. All users:")
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(f"  ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Age: {user[3]}")
        
        # SELECT with WHERE clause
        print("\n2. Users older than 28:")
        cursor.execute("SELECT username, age FROM users WHERE age > 28")
        older_users = cursor.fetchall()
        for user in older_users:
            print(f"  {user[0]} is {user[1]} years old")
        
        # SELECT with ORDER BY
        print("\n3. Posts ordered by creation date:")
        cursor.execute("SELECT title, created_at FROM posts ORDER BY created_at DESC")
        posts = cursor.fetchall()
        for post in posts:
            print(f"  {post[0]} - {post[1]}")
        
        # SELECT with JOIN
        print("\n4. Posts with usernames:")
        cursor.execute("""
            SELECT p.title, u.username, p.created_at 
            FROM posts p 
            JOIN users u ON p.user_id = u.id 
            ORDER BY p.created_at DESC
        """)
        posts_with_users = cursor.fetchall()
        for post in posts_with_users:
            print(f"  '{post[0]}' by {post[1]} on {post[2]}")
        
        # COUNT query
        print("\n5. Statistics:")
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"  Total users: {user_count}")
        
        cursor.execute("SELECT COUNT(*) FROM posts")
        post_count = cursor.fetchone()[0]
        print(f"  Total posts: {post_count}")
        
        cursor.execute("SELECT AVG(age) FROM users")
        avg_age = cursor.fetchone()[0]
        print(f"  Average user age: {avg_age:.1f}")
        
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")

# Run query examples
query_data_examples(conn)

# UPDATING DATA
print("\n--- Updating Data ---")

def update_data_examples(connection):
    """Demonstrate updating data"""
    try:
        cursor = connection.cursor()
        
        # Update a single record
        cursor.execute("UPDATE users SET age = 26 WHERE username = 'alice'")
        print("Updated Alice's age to 26")
        
        # Update multiple records
        cursor.execute("UPDATE posts SET content = content || ' (Updated)' WHERE user_id = 1")
        print("Updated all posts by user 1")
        
        # Commit changes
        connection.commit()
        
        # Verify updates
        cursor.execute("SELECT username, age FROM users WHERE username = 'alice'")
        alice = cursor.fetchone()
        print(f"Alice's new age: {alice[1]}")
        
    except sqlite3.Error as e:
        print(f"Error updating data: {e}")

# Update data
update_data_examples(conn)

# DELETING DATA
print("\n--- Deleting Data ---")

def delete_data_examples(connection):
    """Demonstrate deleting data"""
    try:
        cursor = connection.cursor()
        
        # Count posts before deletion
        cursor.execute("SELECT COUNT(*) FROM posts")
        count_before = cursor.fetchone()[0]
        print(f"Posts before deletion: {count_before}")
        
        # Delete posts older than a certain date (example)
        cursor.execute("DELETE FROM posts WHERE id > 4")
        deleted_rows = cursor.rowcount
        print(f"Deleted {deleted_rows} posts")
        
        # Count posts after deletion
        cursor.execute("SELECT COUNT(*) FROM posts")
        count_after = cursor.fetchone()[0]
        print(f"Posts after deletion: {count_after}")
        
        # Commit changes
        connection.commit()
        
    except sqlite3.Error as e:
        print(f"Error deleting data: {e}")

# Delete data
delete_data_examples(conn)

# DATABASE CLASS FOR BETTER ORGANIZATION
print("\n--- Database Class ---")

class DatabaseManager:
    """A class to manage database operations"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.connect()
    
    def connect(self):
        """Connect to the database"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.connection.row_factory = sqlite3.Row  # Enable column access by name
            print(f"Connected to {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting: {e}")
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Disconnected from database")
    
    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # If it's a SELECT query, return results
            if query.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            else:
                # For INSERT, UPDATE, DELETE, commit and return affected rows
                self.connection.commit()
                return cursor.rowcount
                
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None
    
    def get_user_by_username(self, username):
        """Get user by username"""
        query = "SELECT * FROM users WHERE username = ?"
        result = self.execute_query(query, (username,))
        return result[0] if result else None
    
    def get_posts_by_user(self, user_id):
        """Get all posts by a specific user"""
        query = """
            SELECT p.*, u.username 
            FROM posts p 
            JOIN users u ON p.user_id = u.id 
            WHERE p.user_id = ?
            ORDER BY p.created_at DESC
        """
        return self.execute_query(query, (user_id,))
    
    def add_post(self, user_id, title, content):
        """Add a new post"""
        query = "INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)"
        return self.execute_query(query, (user_id, title, content))
    
    def get_user_statistics(self):
        """Get user statistics"""
        query = """
            SELECT 
                COUNT(*) as total_users,
                AVG(age) as average_age,
                MIN(age) as youngest,
                MAX(age) as oldest
            FROM users
        """
        result = self.execute_query(query)
        return result[0] if result else None

# Use the DatabaseManager class
print("\n--- Using DatabaseManager Class ---")

db = DatabaseManager("learning_db.sqlite")

# Get user by username
alice = db.get_user_by_username('alice')
if alice:
    print(f"Found user: {alice['username']} ({alice['email']})")

# Get posts by user
alice_posts = db.get_posts_by_user(1)
print(f"\nAlice's posts ({len(alice_posts)}):")
for post in alice_posts:
    print(f"  - {post['title']}")

# Add a new post
new_post_id = db.add_post(1, "Python Database Tutorial", "Learning how to work with databases in Python.")
print(f"\nAdded new post with ID: {new_post_id}")

# Get statistics
stats = db.get_user_statistics()
if stats:
    print(f"\nUser Statistics:")
    print(f"  Total users: {stats['total_users']}")
    print(f"  Average age: {stats['average_age']:.1f}")
    print(f"  Age range: {stats['youngest']} - {stats['oldest']}")

# Close connection
db.disconnect()

# TRANSACTIONS
print("\n--- Transactions ---")

def transaction_example():
    """Demonstrate database transactions"""
    conn = create_database_connection("transaction_db.sqlite")
    cursor = conn.cursor()
    
    # Create a simple table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            balance REAL
        )
    """)
    
    # Insert sample data
    cursor.execute("DELETE FROM accounts")  # Clear table
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Alice", 1000.0))
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Bob", 500.0))
    conn.commit()
    
    print("Initial balances:")
    cursor.execute("SELECT name, balance FROM accounts")
    for account in cursor.fetchall():
        print(f"  {account[0]}: ${account[1]}")
    
    # Transfer money with transaction
    try:
        # Begin transaction
        conn.execute("BEGIN TRANSACTION")
        
        # Transfer $200 from Alice to Bob
        cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = 'Alice'")
        cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = 'Bob'")
        
        # Check if Alice has enough money
        cursor.execute("SELECT balance FROM accounts WHERE name = 'Alice'")
        alice_balance = cursor.fetchone()[0]
        
        if alice_balance < 0:
            # Rollback transaction
            conn.rollback()
            print("Transaction rolled back - insufficient funds")
        else:
            # Commit transaction
            conn.commit()
            print("Transaction committed successfully")
            
            print("\nFinal balances:")
            cursor.execute("SELECT name, balance FROM accounts")
            for account in cursor.fetchall():
                print(f"  {account[0]}: ${account[1]}")
                
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Transaction failed: {e}")
    
    conn.close()

# Run transaction example
transaction_example()

# DATABASE BACKUP AND RESTORE
print("\n--- Database Backup and Restore ---")

def backup_database(source_db, backup_file):
    """Create a backup of the database"""
    try:
        source_conn = sqlite3.connect(source_db)
        backup_conn = sqlite3.connect(backup_file)
        
        # Copy database
        source_conn.backup(backup_conn)
        
        source_conn.close()
        backup_conn.close()
        
        print(f"Database backed up to {backup_file}")
        
    except sqlite3.Error as e:
        print(f"Backup failed: {e}")

def restore_database(backup_file, target_db):
    """Restore database from backup"""
    try:
        backup_conn = sqlite3.connect(backup_file)
        target_conn = sqlite3.connect(target_db)
        
        # Copy database
        backup_conn.backup(target_conn)
        
        backup_conn.close()
        target_conn.close()
        
        print(f"Database restored from {backup_file}")
        
    except sqlite3.Error as e:
        print(f"Restore failed: {e}")

# Backup the database
backup_database("learning_db.sqlite", "learning_db_backup.sqlite")

# PRACTICAL PROJECT: SIMPLE BLOG DATABASE
print("\n--- Project: Simple Blog Database ---")

class BlogDatabase:
    """A simple blog database manager"""
    
    def __init__(self, db_name="blog.sqlite"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.setup_tables()
    
    def setup_tables(self):
        """Create blog tables"""
        cursor = self.connection.cursor()
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                bio TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Categories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )
        """)
        
        # Posts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                category_id INTEGER,
                published BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author_id) REFERENCES users (id),
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
        """)
        
        # Comments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER NOT NULL,
                author_name TEXT NOT NULL,
                author_email TEXT NOT NULL,
                content TEXT NOT NULL,
                approved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (post_id) REFERENCES posts (id)
            )
        """)
        
        self.connection.commit()
        print("Blog tables created successfully!")
    
    def add_user(self, username, email, password_hash, bio=None):
        """Add a new user"""
        query = "INSERT INTO users (username, email, password_hash, bio) VALUES (?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(query, (username, email, password_hash, bio))
        self.connection.commit()
        return cursor.lastrowid
    
    def add_category(self, name, description=None):
        """Add a new category"""
        query = "INSERT INTO categories (name, description) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(query, (name, description))
        self.connection.commit()
        return cursor.lastrowid
    
    def add_post(self, title, content, author_id, category_id=None, published=False):
        """Add a new post"""
        query = """
            INSERT INTO posts (title, content, author_id, category_id, published) 
            VALUES (?, ?, ?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (title, content, author_id, category_id, published))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_published_posts(self):
        """Get all published posts with author and category info"""
        query = """
            SELECT p.*, u.username, c.name as category_name
            FROM posts p
            JOIN users u ON p.author_id = u.id
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.published = 1
            ORDER BY p.created_at DESC
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    
    def get_posts_by_category(self, category_name):
        """Get posts by category"""
        query = """
            SELECT p.*, u.username
            FROM posts p
            JOIN users u ON p.author_id = u.id
            JOIN categories c ON p.category_id = c.id
            WHERE c.name = ? AND p.published = 1
            ORDER BY p.created_at DESC
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (category_name,))
        return cursor.fetchall()
    
    def add_comment(self, post_id, author_name, author_email, content):
        """Add a comment to a post"""
        query = "INSERT INTO comments (post_id, author_name, author_email, content) VALUES (?, ?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(query, (post_id, author_name, author_email, content))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_blog_statistics(self):
        """Get blog statistics"""
        cursor = self.connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM posts WHERE published = 1")
        post_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM comments WHERE approved = 1")
        comment_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM categories")
        category_count = cursor.fetchone()[0]
        
        return {
            'users': user_count,
            'posts': post_count,
            'comments': comment_count,
            'categories': category_count
        }
    
    def close(self):
        """Close database connection"""
        self.connection.close()

# Demo the blog database
blog_db = BlogDatabase()

# Add sample data
author_id = blog_db.add_user("john_doe", "john@email.com", "hashed_password", "Tech enthusiast and blogger")
tech_category = blog_db.add_category("Technology", "Posts about technology and programming")
travel_category = blog_db.add_category("Travel", "Travel experiences and tips")

blog_db.add_post("Python for Beginners", "Learn the basics of Python programming...", author_id, tech_category, True)
blog_db.add_post("My Trip to Japan", "Amazing experiences from my recent trip...", author_id, travel_category, True)

# Get published posts
posts = blog_db.get_published_posts()
print(f"\nPublished posts ({len(posts)}):")
for post in posts:
    print(f"  - {post['title']} by {post['username']} in {post['category_name']}")

# Get statistics
stats = blog_db.get_blog_statistics()
print(f"\nBlog Statistics:")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")

blog_db.close()

# BEST PRACTICES
print("\n=== DATABASE BEST PRACTICES ===")
print("1. Always use parameterized queries to prevent SQL injection")
print("2. Use transactions for operations that must succeed or fail together")
print("3. Create indexes on frequently queried columns")
print("4. Always close database connections when done")
print("5. Use appropriate data types for columns")
print("6. Design your schema carefully before creating tables")
print("7. Regular backups are essential")
print("8. Use foreign keys to maintain data integrity")
print("9. Consider using an ORM for complex applications")
print("10. Test your queries with sample data")

print("\n=== Database Operations Complete ===")
print("You now know how to work with SQLite databases in Python!")
