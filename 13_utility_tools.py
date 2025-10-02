# ===========================================
# UTILITY TOOLS - Practical Python Applications
# ===========================================
# This file contains various utility tools and practical applications
# that demonstrate real-world Python programming concepts.
# Each tool is designed to be useful in everyday programming tasks.

print("=== UTILITY TOOLS AND PRACTICAL APPLICATIONS ===")

# Import necessary modules for our utility tools
import os          # For file system operations (checking files, directories)
import json        # For JSON data handling (reading/writing structured data)
import random      # For generating random numbers and choices
import string      # For string manipulation and character sets
import hashlib     # For cryptographic hash functions (MD5, SHA)
import base64      # For base64 encoding/decoding operations
from datetime import datetime, timedelta  # For date and time operations
import csv         # For CSV file reading and writing operations

# PROJECT 1: ENHANCED PASSWORD GENERATOR
print("\n=== PROJECT 1: ENHANCED PASSWORD GENERATOR ===")

class AdvancedPasswordGenerator:
    """
    An advanced password generator with multiple options and security features.
    
    This class provides comprehensive password generation capabilities including:
    - Customizable character sets (uppercase, lowercase, digits, symbols)
    - Exclusion of similar-looking characters (0, O, 1, l, I)
    - Exclusion of ambiguous characters that might be confusing
    - Passphrase generation using common words
    - Password strength analysis and feedback
    """
    
    def __init__(self):
        """
        Initialize the password generator with character sets.
        
        Sets up all the character sets that can be used for password generation:
        - lowercase: All lowercase letters (a-z)
        - uppercase: All uppercase letters (A-Z) 
        - digits: All numeric digits (0-9)
        - symbols: Common special characters for passwords
        - similar_chars: Characters that look alike and might cause confusion
        - ambiguous_chars: Characters that might be confusing in different fonts
        """
        # Define character sets for password generation
        self.lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = string.digits              # '0123456789'
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Common special characters
        
        # Characters that look similar and might cause confusion
        self.similar_chars = "0O1lI"  # Zero looks like O, 1 looks like l or I
        
        # Characters that might be confusing in different fonts or contexts
        self.ambiguous_chars = "{}[]()/\\'\"`~,;.<>"  # Brackets, quotes, punctuation
    
    def generate_password(self, length=12, include_uppercase=True, include_digits=True, 
                         include_symbols=True, exclude_similar=False, exclude_ambiguous=False):
        """
        Generate a secure password with specified criteria.
        
        This method creates a password that meets security requirements by:
        1. Building a character set based on user preferences
        2. Ensuring at least one character from each required type
        3. Filling the remaining length with random characters
        4. Shuffling the final password for randomness
        
        Args:
            length (int): Desired password length (minimum 4)
            include_uppercase (bool): Whether to include uppercase letters
            include_digits (bool): Whether to include numeric digits
            include_symbols (bool): Whether to include special characters
            exclude_similar (bool): Whether to exclude similar-looking characters
            exclude_ambiguous (bool): Whether to exclude ambiguous characters
            
        Returns:
            str: Generated password
            
        Raises:
            ValueError: If no characters are available after exclusions
        """
        
        # Step 1: Build the character set based on user preferences
        # Start with lowercase letters (always included)
        chars = self.lowercase
        
        # Add uppercase letters if requested
        if include_uppercase:
            chars += self.uppercase
            
        # Add digits if requested
        if include_digits:
            chars += self.digits
            
        # Add symbols if requested
        if include_symbols:
            chars += self.symbols
        
        # Step 2: Remove similar characters if requested
        # This helps avoid confusion between characters like 0 and O
        if exclude_similar:
            chars = ''.join(c for c in chars if c not in self.similar_chars)
        
        # Step 3: Remove ambiguous characters if requested
        # This helps avoid confusion with brackets, quotes, etc.
        if exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
        
        # Step 4: Validate that we have characters to work with
        if not chars:
            raise ValueError("No characters available for password generation!")
        
        # Step 5: Ensure minimum password length for security
        if length < 4:
            length = 4
        
        # Step 6: Generate the password
        password = []
        
        # Step 7: Ensure at least one character from each required type
        # This guarantees the password meets complexity requirements
        if include_uppercase:
            password.append(random.choice(self.uppercase))
        if include_digits:
            password.append(random.choice(self.digits))
        if include_symbols:
            password.append(random.choice(self.symbols))
        
        # Step 8: Fill the remaining length with random characters
        # This ensures the password reaches the desired length
        for _ in range(length - len(password)):
            password.append(random.choice(chars))
        
        # Step 9: Shuffle the password to randomize character positions
        # This prevents predictable patterns in the password
        random.shuffle(password)
        
        # Step 10: Return the final password as a string
        return ''.join(password)
    
    def generate_passphrase(self, word_count=4, separator="-", capitalize=True):
        """
        Generate a memorable passphrase using common words.
        
        Passphrases are often easier to remember than random passwords while
        still providing good security. This method creates passphrases by:
        1. Selecting random words from a predefined list
        2. Optionally capitalizing each word
        3. Joining words with a separator
        
        Args:
            word_count (int): Number of words in the passphrase (default 4)
            separator (str): Character to separate words (default "-")
            capitalize (bool): Whether to capitalize each word (default True)
            
        Returns:
            str: Generated passphrase
        """
        
        # Define a list of common, easy-to-remember words
        # These words are chosen to be:
        # - Easy to spell and remember
        # - Common nouns that most people know
        # - Not too long or complex
        words = [
            "apple", "banana", "cherry", "dragon", "eagle", "forest", "garden",
            "house", "island", "jungle", "knight", "ladder", "mountain", "ocean",
            "palace", "queen", "river", "sunset", "tower", "umbrella", "village",
            "wizard", "yellow", "zebra", "castle", "bridge", "crystal", "diamond"
        ]
        
        # Randomly select the specified number of words
        # Using random.sample ensures no word is repeated
        selected_words = random.sample(words, word_count)
        
        # Optionally capitalize each word for better readability
        # This makes the passphrase look more professional
        if capitalize:
            selected_words = [word.capitalize() for word in selected_words]
        
        # Join all words with the specified separator
        # This creates the final passphrase string
        return separator.join(selected_words)
    
    def analyze_password_strength(self, password):
        """
        Analyze password strength and provide detailed feedback.
        
        This method evaluates a password based on multiple security criteria:
        1. Length (longer passwords are generally more secure)
        2. Character variety (mix of different character types)
        3. Pattern avoidance (no repeated characters or common patterns)
        4. Overall complexity score
        
        Args:
            password (str): The password to analyze
            
        Returns:
            dict: Analysis results containing score, strength level, feedback, and length
        """
        
        # Initialize scoring system
        score = 0          # Total security score (0-7)
        feedback = []      # List of improvement suggestions
        
        # CRITERIA 1: Password Length Analysis
        # Longer passwords are exponentially harder to crack
        if len(password) >= 12:
            score += 2  # Excellent length (12+ characters)
        elif len(password) >= 8:
            score += 1  # Good length (8-11 characters)
        else:
            # Password is too short for good security
            feedback.append("Password should be at least 8 characters long")
        
        # CRITERIA 2: Character Variety Analysis
        # Check for presence of different character types
        
        # Check for lowercase letters (a-z)
        if any(c.islower() for c in password):
            score += 1  # Password contains lowercase letters
        else:
            feedback.append("Include lowercase letters")
        
        # Check for uppercase letters (A-Z)
        if any(c.isupper() for c in password):
            score += 1  # Password contains uppercase letters
        else:
            feedback.append("Include uppercase letters")
        
        # Check for numeric digits (0-9)
        if any(c.isdigit() for c in password):
            score += 1  # Password contains numbers
        else:
            feedback.append("Include numbers")
        
        # Check for special characters (!@#$%^&* etc.)
        if any(c in self.symbols for c in password):
            score += 1  # Password contains special characters
        else:
            feedback.append("Include special characters")
        
        # CRITERIA 3: Pattern Analysis
        # Check for repeated consecutive characters (weak pattern)
        if not any(password[i] == password[i+1] for i in range(len(password)-1)):
            score += 1  # No repeated consecutive characters
        else:
            feedback.append("Avoid repeated consecutive characters")
        
        # CRITERIA 4: Common Pattern Detection
        # Check for common weak patterns that attackers might try first
        common_patterns = ["123", "abc", "qwe", "password", "admin"]
        if not any(pattern in password.lower() for pattern in common_patterns):
            score += 1  # No common patterns detected
        else:
            feedback.append("Avoid common patterns")
        
        # CRITERIA 5: Strength Level Assignment
        # Convert numeric score to descriptive strength level
        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
        strength = strength_levels[min(score, len(strength_levels) - 1)]
        
        # Return comprehensive analysis results
        return {
            "score": score,           # Numeric score (0-7)
            "strength": strength,     # Descriptive strength level
            "feedback": feedback,     # List of improvement suggestions
            "length": len(password)   # Password length for reference
        }
    
    def run_generator(self):
        """Run the password generator application"""
        print("Welcome to the Advanced Password Generator!")
        print("=" * 50)
        
        while True:
            print("\nOptions:")
            print("1. Generate random password")
            print("2. Generate passphrase")
            print("3. Analyze password strength")
            print("4. Generate multiple passwords")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                try:
                    length = int(input("Enter password length (default 12): ") or "12")
                    uppercase = input("Include uppercase? (y/n, default y): ").lower() != 'n'
                    digits = input("Include digits? (y/n, default y): ").lower() != 'n'
                    symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
                    exclude_similar = input("Exclude similar characters? (y/n, default n): ").lower() == 'y'
                    exclude_ambiguous = input("Exclude ambiguous characters? (y/n, default n): ").lower() == 'y'
                    
                    password = self.generate_password(length, uppercase, digits, symbols, 
                                                    exclude_similar, exclude_ambiguous)
                    print(f"\nGenerated Password: {password}")
                    
                    # Analyze strength
                    analysis = self.analyze_password_strength(password)
                    print(f"Strength: {analysis['strength']} ({analysis['score']}/7)")
                    
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == '2':
                word_count = int(input("Enter number of words (default 4): ") or "4")
                separator = input("Enter separator (default '-'): ") or "-"
                capitalize = input("Capitalize words? (y/n, default y): ").lower() != 'n'
                
                passphrase = self.generate_passphrase(word_count, separator, capitalize)
                print(f"\nGenerated Passphrase: {passphrase}")
            
            elif choice == '3':
                password = input("Enter password to analyze: ")
                analysis = self.analyze_password_strength(password)
                
                print(f"\nPassword Analysis:")
                print(f"Length: {analysis['length']} characters")
                print(f"Strength: {analysis['strength']} ({analysis['score']}/7)")
                
                if analysis['feedback']:
                    print("Suggestions:")
                    for suggestion in analysis['feedback']:
                        print(f"  • {suggestion}")
                else:
                    print("✓ No suggestions - password looks good!")
            
            elif choice == '4':
                count = int(input("How many passwords to generate? (default 5): ") or "5")
                length = int(input("Password length (default 12): ") or "12")
                
                print(f"\nGenerated {count} passwords:")
                for i in range(count):
                    password = self.generate_password(length)
                    print(f"{i+1}. {password}")
            
            elif choice == '5':
                print("Goodbye! 🔐")
                break
            
            else:
                print("Invalid choice! Please enter 1-5.")

# Demo the password generator
pw_gen = AdvancedPasswordGenerator()
print("Password Generator Demo:")
pw_gen.run_generator()

# PROJECT 2: TEXT ENCRYPTION/DECRYPTION TOOL
print("\n=== PROJECT 2: TEXT ENCRYPTION/DECRYPTION TOOL ===")
# This project demonstrates basic cryptography concepts including:
# - Caesar cipher (substitution cipher)
# - Base64 encoding/decoding
# - Simple hash functions
# - Text transformation techniques

class TextEncryptionTool:
    """
    A simple text encryption and decryption tool using Caesar cipher and base64.
    
    This class provides basic cryptographic functions for educational purposes:
    - Caesar cipher: Shifts letters by a fixed amount
    - Base64 encoding: Converts text to base64 format
    - Hash functions: Creates fixed-length hash values
    - Text transformation: Various encoding/decoding methods
    
    Note: These are basic encryption methods for learning purposes.
    For real security, use professional cryptographic libraries.
    """
    
    def __init__(self):
        """
        Initialize the encryption tool with character sets.
        
        Sets up the alphabet strings needed for Caesar cipher operations:
        - alphabet: lowercase letters for shifting operations
        - alphabet_upper: uppercase letters for shifting operations
        """
        # Define alphabet strings for Caesar cipher operations
        self.alphabet = string.ascii_lowercase      # 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_upper = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def caesar_cipher(self, text, shift, encrypt=True):
        """
        Apply Caesar cipher to text.
        
        The Caesar cipher is one of the oldest encryption methods, where each letter
        in the plaintext is shifted by a fixed number of positions down the alphabet.
        For example, with a shift of 3: A becomes D, B becomes E, etc.
        
        Args:
            text (str): The text to encrypt or decrypt
            shift (int): The number of positions to shift (1-25)
            encrypt (bool): True to encrypt, False to decrypt
            
        Returns:
            str: The encrypted or decrypted text
        """
        result = ""
        
        # Determine the shift direction based on encrypt/decrypt mode
        # For encryption: shift forward, for decryption: shift backward
        shift = shift if encrypt else -shift
        
        # Process each character in the input text
        for char in text:
            # Handle lowercase letters (a-z)
            if char.islower():
                # Find the current position in the alphabet
                current_pos = self.alphabet.index(char)
                # Calculate new position with shift (using modulo 26 for wraparound)
                new_pos = (current_pos + shift) % 26
                # Add the shifted character to result
                result += self.alphabet[new_pos]
                
            # Handle uppercase letters (A-Z)
            elif char.isupper():
                # Find the current position in the uppercase alphabet
                current_pos = self.alphabet_upper.index(char)
                # Calculate new position with shift (using modulo 26 for wraparound)
                new_pos = (current_pos + shift) % 26
                # Add the shifted character to result
                result += self.alphabet_upper[new_pos]
                
            else:
                # Keep non-alphabetic characters unchanged (spaces, numbers, symbols)
                result += char
        
        return result
    
    def base64_encode(self, text):
        """Encode text using base64"""
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    
    def base64_decode(self, encoded_text):
        """Decode base64 text"""
        try:
            return base64.b64decode(encoded_text.encode('utf-8')).decode('utf-8')
        except Exception as e:
            return f"Error decoding: {e}"
    
    def simple_hash(self, text):
        """Generate a simple hash of text"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    
    def run_encryption_tool(self):
        """Run the encryption tool application"""
        print("Welcome to the Text Encryption Tool!")
        print("=" * 40)
        
        while True:
            print("\nOptions:")
            print("1. Caesar Cipher - Encrypt")
            print("2. Caesar Cipher - Decrypt")
            print("3. Base64 Encode")
            print("4. Base64 Decode")
            print("5. Generate Hash")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                text = input("Enter text to encrypt: ")
                shift = int(input("Enter shift value (1-25): "))
                encrypted = self.caesar_cipher(text, shift, True)
                print(f"Encrypted text: {encrypted}")
            
            elif choice == '2':
                text = input("Enter text to decrypt: ")
                shift = int(input("Enter shift value (1-25): "))
                decrypted = self.caesar_cipher(text, shift, False)
                print(f"Decrypted text: {decrypted}")
            
            elif choice == '3':
                text = input("Enter text to encode: ")
                encoded = self.base64_encode(text)
                print(f"Base64 encoded: {encoded}")
            
            elif choice == '4':
                encoded_text = input("Enter base64 text to decode: ")
                decoded = self.base64_decode(encoded_text)
                print(f"Decoded text: {decoded}")
            
            elif choice == '5':
                text = input("Enter text to hash: ")
                hash_value = self.simple_hash(text)
                print(f"MD5 Hash: {hash_value}")
            
            elif choice == '6':
                print("Goodbye! 🔒")
                break
            
            else:
                print("Invalid choice! Please enter 1-6.")

# Demo the encryption tool
encryption_tool = TextEncryptionTool()
print("Encryption Tool Demo:")
encryption_tool.run_encryption_tool()

# PROJECT 3: FILE ORGANIZER
print("\n=== PROJECT 3: FILE ORGANIZER ===")

class FileOrganizer:
    """A tool to organize files by type and date"""
    
    def __init__(self):
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
            'videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv'],
            'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
            'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
            'spreadsheets': ['.xls', '.xlsx', '.csv', '.ods']
        }
    
    def get_file_type(self, filename):
        """Determine file type based on extension"""
        ext = os.path.splitext(filename)[1].lower()
        
        for file_type, extensions in self.file_types.items():
            if ext in extensions:
                return file_type
        
        return 'other'
    
    def organize_directory(self, directory_path, create_subdirs=True):
        """Organize files in a directory by type"""
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist!")
            return
        
        files_organized = 0
        
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Skip directories
            if os.path.isdir(file_path):
                continue
            
            file_type = self.get_file_type(filename)
            
            if create_subdirs:
                # Create subdirectory for file type
                type_dir = os.path.join(directory_path, file_type)
                if not os.path.exists(type_dir):
                    os.makedirs(type_dir)
                    print(f"Created directory: {type_dir}")
                
                # Move file to appropriate directory
                new_path = os.path.join(type_dir, filename)
                if not os.path.exists(new_path):
                    os.rename(file_path, new_path)
                    files_organized += 1
                    print(f"Moved {filename} to {file_type}/")
        
        print(f"\nOrganized {files_organized} files!")
    
    def analyze_directory(self, directory_path):
        """Analyze files in a directory"""
        if not os.path.exists(directory_path):
            print(f"Directory {directory_path} does not exist!")
            return
        
        file_stats = {}
        total_files = 0
        total_size = 0
        
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            if os.path.isfile(file_path):
                file_type = self.get_file_type(filename)
                file_size = os.path.getsize(file_path)
                
                if file_type not in file_stats:
                    file_stats[file_type] = {'count': 0, 'size': 0}
                
                file_stats[file_type]['count'] += 1
                file_stats[file_type]['size'] += file_size
                
                total_files += 1
                total_size += file_size
        
        print(f"\nDirectory Analysis for: {directory_path}")
        print("=" * 50)
        print(f"Total files: {total_files}")
        print(f"Total size: {self.format_size(total_size)}")
        print("\nFile types:")
        
        for file_type, stats in sorted(file_stats.items()):
            percentage = (stats['count'] / total_files) * 100
            print(f"  {file_type}: {stats['count']} files ({percentage:.1f}%) - {self.format_size(stats['size'])}")
    
    def format_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        
        return f"{size_bytes:.1f} {size_names[i]}"
    
    def run_organizer(self):
        """Run the file organizer application"""
        print("Welcome to the File Organizer!")
        print("=" * 30)
        
        while True:
            print("\nOptions:")
            print("1. Analyze directory")
            print("2. Organize directory")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                directory = input("Enter directory path: ").strip()
                self.analyze_directory(directory)
            
            elif choice == '2':
                directory = input("Enter directory path to organize: ").strip()
                confirm = input("This will move files. Continue? (y/n): ").lower()
                if confirm == 'y':
                    self.organize_directory(directory)
                else:
                    print("Operation cancelled.")
            
            elif choice == '3':
                print("Goodbye! 📁")
                break
            
            else:
                print("Invalid choice! Please enter 1-3.")

# Demo the file organizer
file_organizer = FileOrganizer()
print("File Organizer Demo:")
file_organizer.run_organizer()

# PROJECT 4: UNIT CONVERTER
print("\n=== PROJECT 4: UNIT CONVERTER ===")

class UnitConverter:
    """A comprehensive unit converter for various measurements"""
    
    def __init__(self):
        self.conversions = {
            'length': {
                'mm': 0.001,
                'cm': 0.01,
                'm': 1.0,
                'km': 1000.0,
                'inch': 0.0254,
                'foot': 0.3048,
                'yard': 0.9144,
                'mile': 1609.344
            },
            'weight': {
                'mg': 0.001,
                'g': 1.0,
                'kg': 1000.0,
                'oz': 28.3495,
                'lb': 453.592,
                'ton': 1000000.0
            },
            'temperature': {
                'celsius': 'c',
                'fahrenheit': 'f',
                'kelvin': 'k'
            },
            'area': {
                'mm²': 0.000001,
                'cm²': 0.0001,
                'm²': 1.0,
                'km²': 1000000.0,
                'inch²': 0.00064516,
                'foot²': 0.092903,
                'acre': 4046.86
            }
        }
    
    def convert_length(self, value, from_unit, to_unit):
        """Convert length between different units"""
        if from_unit not in self.conversions['length'] or to_unit not in self.conversions['length']:
            return "Invalid units!"
        
        # Convert to meters first
        meters = value * self.conversions['length'][from_unit]
        # Convert to target unit
        result = meters / self.conversions['length'][to_unit]
        
        return f"{value} {from_unit} = {result:.6f} {to_unit}"
    
    def convert_weight(self, value, from_unit, to_unit):
        """Convert weight between different units"""
        if from_unit not in self.conversions['weight'] or to_unit not in self.conversions['weight']:
            return "Invalid units!"
        
        # Convert to grams first
        grams = value * self.conversions['weight'][from_unit]
        # Convert to target unit
        result = grams / self.conversions['weight'][to_unit]
        
        return f"{value} {from_unit} = {result:.6f} {to_unit}"
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Convert temperature between different units"""
        if from_unit not in self.conversions['temperature'] or to_unit not in self.conversions['temperature']:
            return "Invalid units!"
        
        # Convert to Celsius first
        if from_unit == 'celsius':
            celsius = value
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            result = celsius
        elif to_unit == 'fahrenheit':
            result = celsius * 9/5 + 32
        elif to_unit == 'kelvin':
            result = celsius + 273.15
        
        return f"{value}°{from_unit[0].upper()} = {result:.2f}°{to_unit[0].upper()}"
    
    def convert_area(self, value, from_unit, to_unit):
        """Convert area between different units"""
        if from_unit not in self.conversions['area'] or to_unit not in self.conversions['area']:
            return "Invalid units!"
        
        # Convert to square meters first
        sq_meters = value * self.conversions['area'][from_unit]
        # Convert to target unit
        result = sq_meters / self.conversions['area'][to_unit]
        
        return f"{value} {from_unit} = {result:.6f} {to_unit}"
    
    def run_converter(self):
        """Run the unit converter application"""
        print("Welcome to the Unit Converter!")
        print("=" * 30)
        
        while True:
            print("\nConversion Types:")
            print("1. Length")
            print("2. Weight")
            print("3. Temperature")
            print("4. Area")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                print("Available units: mm, cm, m, km, inch, foot, yard, mile")
                value = float(input("Enter value: "))
                from_unit = input("From unit: ").lower()
                to_unit = input("To unit: ").lower()
                result = self.convert_length(value, from_unit, to_unit)
                print(result)
            
            elif choice == '2':
                print("Available units: mg, g, kg, oz, lb, ton")
                value = float(input("Enter value: "))
                from_unit = input("From unit: ").lower()
                to_unit = input("To unit: ").lower()
                result = self.convert_weight(value, from_unit, to_unit)
                print(result)
            
            elif choice == '3':
                print("Available units: celsius, fahrenheit, kelvin")
                value = float(input("Enter value: "))
                from_unit = input("From unit: ").lower()
                to_unit = input("To unit: ").lower()
                result = self.convert_temperature(value, from_unit, to_unit)
                print(result)
            
            elif choice == '4':
                print("Available units: mm², cm², m², km², inch², foot², acre")
                value = float(input("Enter value: "))
                from_unit = input("From unit: ").lower()
                to_unit = input("To unit: ").lower()
                result = self.convert_area(value, from_unit, to_unit)
                print(result)
            
            elif choice == '5':
                print("Goodbye! 📏")
                break
            
            else:
                print("Invalid choice! Please enter 1-5.")

# Demo the unit converter
converter = UnitConverter()
print("Unit Converter Demo:")
converter.run_converter()

print("\n=== ALL UTILITY TOOLS COMPLETED ===")
print("These utility applications demonstrate practical Python programming:")
print("• Advanced string manipulation")
print("• File system operations")
print("• Mathematical calculations")
print("• Data encryption and security")
print("• User interface design")
print("• Error handling and validation")
print("\nThese tools can be extended and customized for specific needs!")
