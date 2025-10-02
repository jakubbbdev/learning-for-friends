  # ===========================================
# GAMES AND APPS - Interactive Python Applications
# ===========================================
# This file contains various interactive games and applications
# that demonstrate Python programming concepts through fun and engaging examples.
# Each project includes user interaction, game logic, and practical programming techniques.

print("=== GAMES AND INTERACTIVE APPS ===")

# Import necessary modules for our games and applications
import random      # For generating random numbers and choices (games, passwords)
import time        # For adding delays and timing in games
import json        # For saving and loading game data (high scores, progress)
import os          # For file system operations (checking files, directories)
from datetime import datetime  # For timestamps and date/time operations
import time

# PROJECT 1: QUIZ APPLICATION
print("\n=== PROJECT 1: QUIZ APPLICATION ===")

class QuizApp:
    """
    A comprehensive quiz application with multiple question types.
    
    This class provides a complete quiz system that includes:
    - Multiple choice questions with explanations
    - Score tracking and progress monitoring
    - Question management and validation
    - User-friendly interface with feedback
    - Extensible question database
    
    The quiz system is designed to be educational and engaging,
    providing immediate feedback and explanations for each answer.
    """
    
    def __init__(self):
        """
        Initialize the quiz application.
        
        Sets up the quiz state variables:
        - questions: List of all quiz questions
        - score: Current user's score (correct answers)
        - current_question: Index of the current question being displayed
        """
        # Initialize quiz state variables
        self.questions = []        # List to store all quiz questions
        self.score = 0            # User's current score (number of correct answers)
        self.current_question = 0 # Index of the current question (0-based)
        
        # Load sample questions to get started
        self.load_sample_questions()
    
    def load_sample_questions(self):
        """Load sample quiz questions"""
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct": 2,
                "explanation": "Paris is the capital and largest city of France."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct": 1,
                "explanation": "Mars is called the Red Planet due to iron oxide on its surface."
            },
            {
                "question": "What is 15 + 27?",
                "options": ["40", "41", "42", "43"],
                "correct": 2,
                "explanation": "15 + 27 = 42"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Van Gogh", "Picasso", "Da Vinci", "Michelangelo"],
                "correct": 2,
                "explanation": "Leonardo da Vinci painted the Mona Lisa in the early 16th century."
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct": 1,
                "explanation": "The blue whale is the largest mammal and animal on Earth."
            }
        ]
    
    def display_question(self, question_num):
        """Display a question with options"""
        if question_num >= len(self.questions):
            return False
        
        q = self.questions[question_num]
        print(f"\nQuestion {question_num + 1}/{len(self.questions)}")
        print(f"{q['question']}")
        print("-" * 50)
        
        for i, option in enumerate(q['options']):
            print(f"{i + 1}. {option}")
        
        return True
    
    def check_answer(self, question_num, user_answer):
        """Check if the user's answer is correct"""
        if question_num >= len(self.questions):
            return False
        
        q = self.questions[question_num]
        correct_answer = q['correct'] + 1  # Convert to 1-based indexing
        
        if user_answer == correct_answer:
            print("✓ Correct!")
            self.score += 1
        else:
            print(f"✗ Wrong! The correct answer was: {q['options'][q['correct']]}")
        
        print(f"Explanation: {q['explanation']}")
        return user_answer == correct_answer
    
    def run_quiz(self):
        """Run the complete quiz"""
        print("Welcome to the Quiz Application!")
        print("Answer the questions by entering the number of your choice.")
        print("=" * 60)
        
        self.score = 0
        self.current_question = 0
        
        for i in range(len(self.questions)):
            if not self.display_question(i):
                break
            
            while True:
                try:
                    user_input = input("\nYour answer (1-4): ").strip()
                    answer = int(user_input)
                    
                    if 1 <= answer <= 4:
                        self.check_answer(i, answer)
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")
            
            time.sleep(1)  # Brief pause between questions
        
        self.show_results()
    
    def show_results(self):
        """Display quiz results"""
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        
        print("\n" + "=" * 60)
        print("QUIZ RESULTS")
        print("=" * 60)
        print(f"Total Questions: {total_questions}")
        print(f"Correct Answers: {self.score}")
        print(f"Wrong Answers: {total_questions - self.score}")
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 80:
            print("🎉 Excellent! You did great!")
        elif percentage >= 60:
            print("👍 Good job! You passed!")
        else:
            print("📚 Keep studying! You can do better next time!")
    
    def add_question(self, question, options, correct_index, explanation=""):
        """Add a new question to the quiz"""
        new_question = {
            "question": question,
            "options": options,
            "correct": correct_index,
            "explanation": explanation
        }
        self.questions.append(new_question)
        print(f"Added new question: {question}")

# Demo the quiz app
quiz = QuizApp()
print("Quiz Application Demo:")
quiz.run_quiz()

# PROJECT 2: HANGMAN GAME
print("\n=== PROJECT 2: HANGMAN GAME ===")

class HangmanGame:
    """A classic hangman word guessing game"""
    
    def __init__(self):
        self.words = [
            "python", "programming", "computer", "algorithm", "function",
            "variable", "dictionary", "list", "string", "integer",
            "boolean", "class", "object", "method", "inheritance"
        ]
        self.word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
    
    def select_random_word(self):
        """Select a random word from the word list"""
        self.word = random.choice(self.words).lower()
        self.guessed_letters = set()
        self.wrong_guesses = 0
    
    def display_word(self):
        """Display the word with guessed letters revealed"""
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def display_hangman(self):
        """Display the hangman drawing based on wrong guesses"""
        hangman_parts = [
            "   +---+",
            "   |   |",
            "   O   |",
            "  /|\\  |",
            "  / \\  |",
            "       |",
            "========="
        ]
        
        print("\nHangman:")
        for i, line in enumerate(hangman_parts):
            if i == 0 or i == 1 or i == 5 or i == 6:  # Always show base
                print(line)
            elif i == 2 and self.wrong_guesses >= 1:  # Head
                print(line)
            elif i == 3 and self.wrong_guesses >= 2:  # Body and arms
                print(line)
            elif i == 4 and self.wrong_guesses >= 4:  # Legs
                print(line)
            else:
                print("       |")
    
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.lower()
        
        if letter in self.guessed_letters:
            print(f"You already guessed '{letter}'!")
            return False
        
        self.guessed_letters.add(letter)
        
        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            return True
        else:
            print(f"Sorry, '{letter}' is not in the word.")
            self.wrong_guesses += 1
            return False
    
    def is_game_won(self):
        """Check if the game is won"""
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_game_lost(self):
        """Check if the game is lost"""
        return self.wrong_guesses >= self.max_wrong_guesses
    
    def play_game(self):
        """Play a complete hangman game"""
        print("Welcome to Hangman!")
        print("Guess the word by entering letters. You have 6 wrong guesses allowed.")
        print("=" * 60)
        
        self.select_random_word()
        
        while not self.is_game_won() and not self.is_game_lost():
            print(f"\nWord: {self.display_word()}")
            print(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")
            print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
            
            self.display_hangman()
            
            guess = input("\nEnter a letter: ").strip().lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue
            
            self.make_guess(guess)
        
        # Game over
        print(f"\nFinal word: {self.word}")
        
        if self.is_game_won():
            print("🎉 Congratulations! You won!")
        else:
            print("💀 Game Over! You lost!")
            self.display_hangman()

# Demo the hangman game
hangman = HangmanGame()
print("Hangman Game Demo:")
hangman.play_game()

# PROJECT 3: TIC-TAC-TOE GAME
print("\n=== PROJECT 3: TIC-TAC-TOE GAME ===")

class TicTacToe:
    """A classic tic-tac-toe game for two players"""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
    
    def display_board(self):
        """Display the current game board"""
        print("\nCurrent Board:")
        print("  1   2   3")
        for i, row in enumerate(self.board):
            print(f"{i+1} {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  ---------")
    
    def make_move(self, row, col):
        """Make a move on the board"""
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            print("Invalid position! Please enter row and column between 1-3.")
            return False
        
        if self.board[row][col] != ' ':
            print("That position is already taken!")
            return False
        
        self.board[row][col] = self.current_player
        return True
    
    def check_winner(self):
        """Check if there's a winner"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """Check if the board is full"""
        return all(cell != ' ' for row in self.board for cell in row)
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play_game(self):
        """Play a complete tic-tac-toe game"""
        print("Welcome to Tic-Tac-Toe!")
        print("Players take turns. Enter row and column (1-3) to make your move.")
        print("=" * 50)
        
        while not self.game_over:
            self.display_board()
            print(f"\nPlayer {self.current_player}'s turn")
            
            while True:
                try:
                    row = int(input("Enter row (1-3): ")) - 1
                    col = int(input("Enter column (1-3): ")) - 1
                    
                    if self.make_move(row, col):
                        break
                except ValueError:
                    print("Please enter valid numbers!")
            
            # Check for winner
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"🎉 Player {winner} wins!")
                self.game_over = True
            elif self.is_board_full():
                self.display_board()
                print("🤝 It's a tie!")
                self.game_over = True
            else:
                self.switch_player()

# Demo the tic-tac-toe game
tic_tac_toe = TicTacToe()
print("Tic-Tac-Toe Game Demo:")
tic_tac_toe.play_game()

# PROJECT 4: WEATHER INFORMATION APP
print("\n=== PROJECT 4: WEATHER INFORMATION APP ===")

class WeatherApp:
    """A simple weather information application with mock data"""
    
    def __init__(self):
        self.cities = {
            "new york": {"temp": 22, "condition": "Sunny", "humidity": 65, "wind": 12},
            "london": {"temp": 15, "condition": "Cloudy", "humidity": 80, "wind": 8},
            "tokyo": {"temp": 28, "condition": "Rainy", "humidity": 90, "wind": 15},
            "paris": {"temp": 18, "condition": "Partly Cloudy", "humidity": 70, "wind": 10},
            "sydney": {"temp": 25, "condition": "Sunny", "humidity": 60, "wind": 14},
            "berlin": {"temp": 16, "condition": "Overcast", "humidity": 75, "wind": 9}
        }
        self.favorites = []
    
    def get_weather(self, city):
        """Get weather information for a city"""
        city_lower = city.lower()
        if city_lower in self.cities:
            return self.cities[city_lower]
        return None
    
    def display_weather(self, city, weather_data):
        """Display weather information in a formatted way"""
        print(f"\n🌤️  Weather for {city.title()}")
        print("=" * 40)
        print(f"Temperature: {weather_data['temp']}°C")
        print(f"Condition: {weather_data['condition']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']} km/h")
        
        # Add weather emoji based on condition
        condition_emojis = {
            "sunny": "☀️",
            "cloudy": "☁️",
            "rainy": "🌧️",
            "partly cloudy": "⛅",
            "overcast": "☁️"
        }
        
        condition_lower = weather_data['condition'].lower()
        emoji = condition_emojis.get(condition_lower, "🌤️")
        print(f"Weather: {emoji} {weather_data['condition']}")
    
    def add_favorite(self, city):
        """Add a city to favorites"""
        if city.lower() in self.cities and city.lower() not in self.favorites:
            self.favorites.append(city.lower())
            print(f"Added {city.title()} to favorites!")
        else:
            print("City not found or already in favorites!")
    
    def remove_favorite(self, city):
        """Remove a city from favorites"""
        if city.lower() in self.favorites:
            self.favorites.remove(city.lower())
            print(f"Removed {city.title()} from favorites!")
        else:
            print("City not in favorites!")
    
    def show_favorites(self):
        """Display favorite cities"""
        if self.favorites:
            print("\n⭐ Favorite Cities:")
            for city in self.favorites:
                weather = self.get_weather(city)
                if weather:
                    print(f"  {city.title()}: {weather['temp']}°C, {weather['condition']}")
        else:
            print("No favorite cities yet!")
    
    def run_app(self):
        """Run the weather application"""
        print("Welcome to the Weather Information App!")
        print("Available cities: New York, London, Tokyo, Paris, Sydney, Berlin")
        print("=" * 60)
        
        while True:
            print("\nOptions:")
            print("1. Check weather for a city")
            print("2. Add city to favorites")
            print("3. Remove city from favorites")
            print("4. Show favorite cities")
            print("5. Show all cities")
            print("6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                city = input("Enter city name: ").strip()
                weather = self.get_weather(city)
                if weather:
                    self.display_weather(city, weather)
                else:
                    print("City not found!")
            
            elif choice == '2':
                city = input("Enter city name to add to favorites: ").strip()
                self.add_favorite(city)
            
            elif choice == '3':
                city = input("Enter city name to remove from favorites: ").strip()
                self.remove_favorite(city)
            
            elif choice == '4':
                self.show_favorites()
            
            elif choice == '5':
                print("\nAll Available Cities:")
                for city, weather in self.cities.items():
                    print(f"  {city.title()}: {weather['temp']}°C, {weather['condition']}")
            
            elif choice == '6':
                print("Goodbye! 👋")
                break
            
            else:
                print("Invalid choice! Please enter 1-6.")

# Demo the weather app
weather_app = WeatherApp()
print("Weather App Demo:")
weather_app.run_app()

# PROJECT 5: NOTE-TAKING APPLICATION
print("\n=== PROJECT 5: NOTE-TAKING APPLICATION ===")

class NoteTakingApp:
    """A comprehensive note-taking application with categories and search"""
    
    def __init__(self):
        self.notes = []
        self.categories = set()
        self.filename = "notes.json"
        self.load_notes()
    
    def load_notes(self):
        """Load notes from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    self.notes = json.load(file)
                print(f"Loaded {len(self.notes)} notes from file.")
            else:
                print("No existing notes file found. Starting fresh!")
        except Exception as e:
            print(f"Error loading notes: {e}")
            self.notes = []
    
    def save_notes(self):
        """Save notes to file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.notes, file, indent=2, ensure_ascii=False)
            print("Notes saved successfully!")
        except Exception as e:
            print(f"Error saving notes: {e}")
    
    def create_note(self, title, content, category="General"):
        """Create a new note"""
        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "category": category,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.notes.append(note)
        self.categories.add(category)
        print(f"Created note: '{title}' in category '{category}'")
        self.save_notes()
    
    def edit_note(self, note_id, new_title=None, new_content=None, new_category=None):
        """Edit an existing note"""
        for note in self.notes:
            if note["id"] == note_id:
                if new_title:
                    note["title"] = new_title
                if new_content:
                    note["content"] = new_content
                if new_category:
                    note["category"] = new_category
                    self.categories.add(new_category)
                
                note["updated_at"] = datetime.now().isoformat()
                print(f"Updated note ID {note_id}")
                self.save_notes()
                return True
        
        print(f"Note with ID {note_id} not found!")
        return False
    
    def delete_note(self, note_id):
        """Delete a note"""
        for i, note in enumerate(self.notes):
            if note["id"] == note_id:
                deleted_note = self.notes.pop(i)
                print(f"Deleted note: '{deleted_note['title']}'")
                self.save_notes()
                return True
        
        print(f"Note with ID {note_id} not found!")
        return False
    
    def search_notes(self, search_term):
        """Search notes by title or content"""
        search_term_lower = search_term.lower()
        matching_notes = []
        
        for note in self.notes:
            if (search_term_lower in note["title"].lower() or 
                search_term_lower in note["content"].lower()):
                matching_notes.append(note)
        
        return matching_notes
    
    def filter_by_category(self, category):
        """Filter notes by category"""
        return [note for note in self.notes if note["category"].lower() == category.lower()]
    
    def display_note(self, note):
        """Display a single note"""
        print(f"\n📝 Note ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Category: {note['category']}")
        print(f"Created: {note['created_at'][:19]}")
        print(f"Updated: {note['updated_at'][:19]}")
        print(f"Content: {note['content']}")
        print("-" * 50)
    
    def display_all_notes(self):
        """Display all notes"""
        if not self.notes:
            print("No notes found!")
            return
        
        print(f"\n📚 All Notes ({len(self.notes)} total):")
        for note in self.notes:
            self.display_note(note)
    
    def run_app(self):
        """Run the note-taking application"""
        print("Welcome to the Note-Taking Application!")
        print("=" * 50)
        
        while True:
            print("\nOptions:")
            print("1. Create new note")
            print("2. Edit note")
            print("3. Delete note")
            print("4. View all notes")
            print("5. Search notes")
            print("6. Filter by category")
            print("7. Show categories")
            print("8. Exit")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                title = input("Enter note title: ").strip()
                content = input("Enter note content: ").strip()
                category = input("Enter category (or press Enter for 'General'): ").strip()
                if not category:
                    category = "General"
                self.create_note(title, content, category)
            
            elif choice == '2':
                try:
                    note_id = int(input("Enter note ID to edit: "))
                    new_title = input("Enter new title (or press Enter to keep current): ").strip()
                    new_content = input("Enter new content (or press Enter to keep current): ").strip()
                    new_category = input("Enter new category (or press Enter to keep current): ").strip()
                    
                    self.edit_note(
                        note_id,
                        new_title if new_title else None,
                        new_content if new_content else None,
                        new_category if new_category else None
                    )
                except ValueError:
                    print("Please enter a valid note ID!")
            
            elif choice == '3':
                try:
                    note_id = int(input("Enter note ID to delete: "))
                    self.delete_note(note_id)
                except ValueError:
                    print("Please enter a valid note ID!")
            
            elif choice == '4':
                self.display_all_notes()
            
            elif choice == '5':
                search_term = input("Enter search term: ").strip()
                matching_notes = self.search_notes(search_term)
                if matching_notes:
                    print(f"\nFound {len(matching_notes)} matching notes:")
                    for note in matching_notes:
                        self.display_note(note)
                else:
                    print("No notes found matching your search!")
            
            elif choice == '6':
                category = input("Enter category to filter by: ").strip()
                filtered_notes = self.filter_by_category(category)
                if filtered_notes:
                    print(f"\nNotes in category '{category}':")
                    for note in filtered_notes:
                        self.display_note(note)
                else:
                    print(f"No notes found in category '{category}'!")
            
            elif choice == '7':
                if self.categories:
                    print(f"\nAvailable categories: {', '.join(sorted(self.categories))}")
                else:
                    print("No categories yet!")
            
            elif choice == '8':
                print("Goodbye! Your notes have been saved. 👋")
                break
            
            else:
                print("Invalid choice! Please enter 1-8.")

# Demo the note-taking app
note_app = NoteTakingApp()
print("Note-Taking App Demo:")
note_app.run_app()

print("\n=== ALL GAMES AND APPS COMPLETED ===")
print("These interactive applications demonstrate various Python concepts:")
print("• Object-oriented programming")
print("• User input handling")
print("• File I/O operations")
print("• Data structures and algorithms")
print("• Error handling")
print("• JSON data management")
print("• Game logic and state management")
print("\nTry running each application and modify them to learn more!")
