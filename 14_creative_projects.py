# ===========================================
# CREATIVE PROJECTS - Fun and Interactive Python Applications
# ===========================================
# This file contains creative and artistic Python applications that demonstrate
# how programming can be used for fun, visual effects, and creative expression.
# Each project combines technical skills with artistic and creative elements.

print("=== CREATIVE AND FUN PYTHON PROJECTS ===")

# Import necessary modules for our creative projects
import random      # For generating random elements (colors, animations, stories)
import time        # For timing animations and delays
import json        # For storing creative data (stories, configurations)
import os          # For file system operations
from datetime import datetime, timedelta  # For time-based creative elements
import math        # For mathematical calculations (circles, geometry)

# PROJECT 1: ASCII ART GENERATOR
print("\n=== PROJECT 1: ASCII ART GENERATOR ===")

class ASCIIArtGenerator:
    """
    Generate ASCII art from text and create simple drawings.
    
    This class provides tools for creating ASCII art, including:
    - Text-to-ASCII conversion using custom fonts
    - Simple geometric shape generation
    - Block-style character rendering
    - Extensible font system for different styles
    
    ASCII art is a graphic design technique that uses printable characters
    to create images and text art, popular in early computing and terminal interfaces.
    """
    
    def __init__(self):
        """
        Initialize the ASCII art generator with font definitions.
        
        Sets up the font dictionary containing character mappings.
        Each character is represented as a list of 5 strings (lines),
        where each string represents one horizontal line of the character.
        """
        # Define font styles for ASCII art generation
        # Each font contains character mappings where each character
        # is represented as a list of 5 lines (strings)
        self.fonts = {
            'block': {
                # Block-style font using Unicode block characters (█)
                # Each character is 6 characters wide and 5 lines tall
                'A': ['  ██  ', ' ████ ', '██  ██', '██████', '██  ██'],  # Letter A
                'B': ['█████ ', '██  ██', '█████ ', '██  ██', '█████ '],  # Letter B
                'C': [' █████', '██    ', '██    ', '██    ', ' █████'],  # Letter C
                'D': ['█████ ', '██  ██', '██  ██', '██  ██', '█████ '],  # Letter D
                'E': ['██████', '██    ', '█████ ', '██    ', '██████'],  # Letter E
                'F': ['██████', '██    ', '█████ ', '██    ', '██    '],  # Letter F
                'G': [' █████', '██    ', '██ ███', '██  ██', ' █████'],  # Letter G
                'H': ['██  ██', '██  ██', '██████', '██  ██', '██  ██'],  # Letter H
                'I': ['██████', '  ██  ', '  ██  ', '  ██  ', '██████'],  # Letter I
                'J': ['██████', '    ██', '    ██', '██  ██', ' ████ '],  # Letter J
                'K': ['██  ██', '██ ██ ', '████  ', '██ ██ ', '██  ██'],  # Letter K
                'L': ['██    ', '██    ', '██    ', '██    ', '██████'],  # Letter L
                'M': ['██  ██', '██████', '██ ████', '██  ██', '██  ██'],  # Letter M
                'N': ['██  ██', '███ ██', '██ ████', '██  ██', '██  ██'],  # Letter N
                'O': [' █████', '██  ██', '██  ██', '██  ██', ' █████'],  # Letter O
                'P': ['█████ ', '██  ██', '█████ ', '██    ', '██    '],  # Letter P
                'Q': [' █████', '██  ██', '██ ███', '██ ██ ', ' █████'],  # Letter Q
                'R': ['█████ ', '██  ██', '█████ ', '██ ██ ', '██  ██'],  # Letter R
                'S': [' █████', '██    ', ' █████', '    ██', ' █████'],  # Letter S
                'T': ['██████', '  ██  ', '  ██  ', '  ██  ', '  ██  '],  # Letter T
                'U': ['██  ██', '██  ██', '██  ██', '██  ██', ' █████'],  # Letter U
                'V': ['██  ██', '██  ██', '██  ██', ' ████ ', '  ██  '],  # Letter V
                'W': ['██  ██', '██  ██', '██ ████', '██████', '██  ██'],  # Letter W
                'X': ['██  ██', ' ████ ', '  ██  ', ' ████ ', '██  ██'],  # Letter X
                'Y': ['██  ██', '██  ██', ' ████ ', '  ██  ', '  ██  '],  # Letter Y
                'Z': ['██████', '    ██', '  ██  ', '██    ', '██████'],  # Letter Z
                ' ': ['      ', '      ', '      ', '      ', '      ']   # Space character
            }
        }
    
    def text_to_ascii(self, text, font='block'):
        """Convert text to ASCII art"""
        text = text.upper()
        lines = [''] * 5  # Each character is 5 lines tall
        
        for char in text:
            if char in self.fonts[font]:
                for i, line in enumerate(self.fonts[font][char]):
                    lines[i] += line
            else:
                # Use space for unknown characters
                for i in range(5):
                    lines[i] += '      '
        
        return '\n'.join(lines)
    
    def create_simple_drawing(self, shape, size=5):
        """Create simple ASCII drawings"""
        if shape == 'square':
            return self.draw_square(size)
        elif shape == 'triangle':
            return self.draw_triangle(size)
        elif shape == 'diamond':
            return self.draw_diamond(size)
        elif shape == 'circle':
            return self.draw_circle(size)
        else:
            return "Unknown shape!"
    
    def draw_square(self, size):
        """Draw a square"""
        result = []
        for i in range(size):
            if i == 0 or i == size - 1:
                result.append('█' * size)
            else:
                result.append('█' + ' ' * (size - 2) + '█')
        return '\n'.join(result)
    
    def draw_triangle(self, size):
        """Draw a triangle"""
        result = []
        for i in range(size):
            spaces = size - i - 1
            chars = 2 * i + 1
            result.append(' ' * spaces + '█' * chars)
        return '\n'.join(result)
    
    def draw_diamond(self, size):
        """Draw a diamond"""
        result = []
        # Upper half
        for i in range(size):
            spaces = size - i - 1
            chars = 2 * i + 1
            result.append(' ' * spaces + '█' * chars)
        # Lower half
        for i in range(size - 2, -1, -1):
            spaces = size - i - 1
            chars = 2 * i + 1
            result.append(' ' * spaces + '█' * chars)
        return '\n'.join(result)
    
    def draw_circle(self, radius):
        """Draw a simple circle"""
        result = []
        for y in range(-radius, radius + 1):
            line = ''
            for x in range(-radius, radius + 1):
                if abs(math.sqrt(x*x + y*y) - radius) < 0.5:
                    line += '█'
                else:
                    line += ' '
            result.append(line)
        return '\n'.join(result)
    
    def run_generator(self):
        """Run the ASCII art generator"""
        print("Welcome to the ASCII Art Generator!")
        print("=" * 40)
        
        while True:
            print("\nOptions:")
            print("1. Convert text to ASCII art")
            print("2. Create simple drawings")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                text = input("Enter text to convert: ")
                ascii_art = self.text_to_ascii(text)
                print(f"\nASCII Art:\n{ascii_art}")
            
            elif choice == '2':
                print("Available shapes: square, triangle, diamond, circle")
                shape = input("Enter shape: ").lower()
                try:
                    size = int(input("Enter size (default 5): ") or "5")
                    drawing = self.create_simple_drawing(shape, size)
                    print(f"\n{shape.title()}:\n{drawing}")
                except ValueError:
                    print("Invalid size!")
            
            elif choice == '3':
                print("Goodbye! 🎨")
                break
            
            else:
                print("Invalid choice! Please enter 1-3.")

# Demo the ASCII art generator
ascii_gen = ASCIIArtGenerator()
print("ASCII Art Generator Demo:")
ascii_gen.run_generator()

# PROJECT 2: COLORFUL TEXT DISPLAY
print("\n=== PROJECT 2: COLORFUL TEXT DISPLAY ===")

class ColorfulTextDisplay:
    """Display text with various colors and effects using ANSI escape codes"""
    
    def __init__(self):
        self.colors = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bright_black': '\033[90m',
            'bright_red': '\033[91m',
            'bright_green': '\033[92m',
            'bright_yellow': '\033[93m',
            'bright_blue': '\033[94m',
            'bright_magenta': '\033[95m',
            'bright_cyan': '\033[96m',
            'bright_white': '\033[97m'
        }
        
        self.styles = {
            'normal': '\033[0m',
            'bold': '\033[1m',
            'dim': '\033[2m',
            'italic': '\033[3m',
            'underline': '\033[4m',
            'blink': '\033[5m',
            'reverse': '\033[7m'
        }
        
        self.backgrounds = {
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'yellow': '\033[43m',
            'blue': '\033[44m',
            'magenta': '\033[45m',
            'cyan': '\033[46m',
            'white': '\033[47m'
        }
    
    def colorize_text(self, text, color='white', style='normal', background=None):
        """Apply color and style to text"""
        color_code = self.colors.get(color, self.colors['white'])
        style_code = self.styles.get(style, self.styles['normal'])
        bg_code = self.backgrounds.get(background, '') if background else ''
        reset_code = self.styles['normal']
        
        return f"{color_code}{style_code}{bg_code}{text}{reset_code}"
    
    def rainbow_text(self, text):
        """Create rainbow colored text"""
        rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
        result = ''
        
        for i, char in enumerate(text):
            color = rainbow_colors[i % len(rainbow_colors)]
            result += self.colorize_text(char, color)
        
        return result
    
    def gradient_text(self, text, start_color='red', end_color='blue'):
        """Create gradient colored text"""
        colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
        
        try:
            start_idx = colors.index(start_color)
            end_idx = colors.index(end_color)
        except ValueError:
            start_idx, end_idx = 0, 5
        
        result = ''
        text_len = len(text)
        
        for i, char in enumerate(text):
            if text_len > 1:
                color_idx = start_idx + (end_idx - start_idx) * i / (text_len - 1)
                color_idx = int(color_idx) % len(colors)
            else:
                color_idx = start_idx
            
            color = colors[color_idx]
            result += self.colorize_text(char, color)
        
        return result
    
    def animated_text(self, text, delay=0.1):
        """Display text with animation effect"""
        for i in range(len(text) + 1):
            print(f"\r{text[:i]}", end='', flush=True)
            time.sleep(delay)
        print()
    
    def typewriter_effect(self, text, delay=0.05):
        """Display text with typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def display_demo(self):
        """Display various text effects"""
        print("Colorful Text Display Demo:")
        print("=" * 40)
        
        # Basic colors
        print("\nBasic Colors:")
        for color_name, color_code in self.colors.items():
            if not color_name.startswith('bright_'):
                print(self.colorize_text(f"  {color_name.title()}", color_name))
        
        # Styles
        print("\nText Styles:")
        print(self.colorize_text("  Normal text", 'white', 'normal'))
        print(self.colorize_text("  Bold text", 'white', 'bold'))
        print(self.colorize_text("  Dim text", 'white', 'dim'))
        print(self.colorize_text("  Italic text", 'white', 'italic'))
        print(self.colorize_text("  Underlined text", 'white', 'underline'))
        print(self.colorize_text("  Blinking text", 'white', 'blink'))
        
        # Rainbow text
        print(f"\nRainbow Text: {self.rainbow_text('Hello World!')}")
        
        # Gradient text
        print(f"\nGradient Text: {self.gradient_text('Python Programming', 'red', 'blue')}")
        
        # Animated text
        print("\nAnimated Text:")
        self.animated_text("This text appears letter by letter!")
        
        # Typewriter effect
        print("\nTypewriter Effect:")
        self.typewriter_effect("This text appears with typewriter effect!")

# Demo the colorful text display
color_display = ColorfulTextDisplay()
color_display.display_demo()

# PROJECT 3: SIMPLE ANIMATION SYSTEM
print("\n=== PROJECT 3: SIMPLE ANIMATION SYSTEM ===")

class SimpleAnimation:
    """Create simple text-based animations"""
    
    def __init__(self):
        self.frames = []
    
    def loading_spinner(self, duration=5):
        """Display a loading spinner animation"""
        spinner_chars = ['|', '/', '-', '\\']
        start_time = time.time()
        
        print("Loading", end='', flush=True)
        
        while time.time() - start_time < duration:
            for char in spinner_chars:
                print(f'\rLoading {char}', end='', flush=True)
                time.sleep(0.1)
        
        print('\rLoading complete! ✓')
    
    def progress_bar(self, total=100, duration=5):
        """Display a progress bar animation"""
        start_time = time.time()
        bar_length = 30
        
        for i in range(total + 1):
            elapsed = time.time() - start_time
            if elapsed >= duration:
                break
            
            # Calculate progress
            progress = i / total
            filled_length = int(bar_length * progress)
            
            # Create progress bar
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            percentage = progress * 100
            
            print(f'\rProgress: |{bar}| {percentage:.1f}%', end='', flush=True)
            time.sleep(duration / total)
        
        print('\rProgress: |' + '█' * bar_length + '| 100.0% Complete! ✓')
    
    def bouncing_ball(self, duration=10):
        """Display a bouncing ball animation"""
        start_time = time.time()
        position = 0
        direction = 1
        max_position = 20
        
        print("Bouncing Ball Animation:")
        print("Press Ctrl+C to stop")
        
        try:
            while time.time() - start_time < duration:
                # Clear screen (works on most terminals)
                print('\033[2J\033[H', end='')
                
                # Create the ball line
                line = [' '] * max_position
                line[position] = '●'
                
                print(''.join(line))
                print('─' * max_position)
                
                # Update position
                position += direction
                if position >= max_position - 1 or position <= 0:
                    direction *= -1
                
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\nAnimation stopped!")
    
    def matrix_rain(self, duration=10):
        """Display Matrix-style falling characters"""
        start_time = time.time()
        width = 50
        height = 20
        
        # Initialize columns
        columns = [0] * width
        
        print("Matrix Rain Animation:")
        print("Press Ctrl+C to stop")
        
        try:
            while time.time() - start_time < duration:
                # Clear screen
                print('\033[2J\033[H', end='')
                
                # Create matrix effect
                for row in range(height):
                    line = ''
                    for col in range(width):
                        if random.random() < 0.1:  # Random character
                            char = chr(random.randint(33, 126))
                            line += char
                        else:
                            line += ' '
                    print(line)
                
                time.sleep(0.1)
        
        except KeyboardInterrupt:
            print("\nAnimation stopped!")
    
    def run_animation_demo(self):
        """Run animation demonstrations"""
        print("Welcome to the Simple Animation System!")
        print("=" * 40)
        
        while True:
            print("\nAvailable Animations:")
            print("1. Loading Spinner")
            print("2. Progress Bar")
            print("3. Bouncing Ball")
            print("4. Matrix Rain")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                duration = int(input("Enter duration in seconds (default 5): ") or "5")
                self.loading_spinner(duration)
            
            elif choice == '2':
                duration = int(input("Enter duration in seconds (default 5): ") or "5")
                self.progress_bar(100, duration)
            
            elif choice == '3':
                duration = int(input("Enter duration in seconds (default 10): ") or "10")
                self.bouncing_ball(duration)
            
            elif choice == '4':
                duration = int(input("Enter duration in seconds (default 10): ") or "10")
                self.matrix_rain(duration)
            
            elif choice == '5':
                print("Goodbye! 🎬")
                break
            
            else:
                print("Invalid choice! Please enter 1-5.")

# Demo the animation system
animator = SimpleAnimation()
print("Animation System Demo:")
animator.run_animation_demo()

# PROJECT 4: INTERACTIVE STORY GENERATOR
print("\n=== PROJECT 4: INTERACTIVE STORY GENERATOR ===")

class StoryGenerator:
    """Generate interactive stories with user choices"""
    
    def __init__(self):
        self.stories = {
            'adventure': {
                'title': 'The Mysterious Forest',
                'start': 'You find yourself at the edge of a dark forest. A path leads into the trees.',
                'choices': {
                    '1': {
                        'text': 'Follow the path into the forest',
                        'next': 'forest_path'
                    },
                    '2': {
                        'text': 'Look for another way around',
                        'next': 'around_forest'
                    }
                }
            },
            'forest_path': {
                'text': 'You walk deeper into the forest. You hear strange sounds ahead.',
                'choices': {
                    '1': {
                        'text': 'Investigate the sounds',
                        'next': 'investigate'
                    },
                    '2': {
                        'text': 'Try to sneak past quietly',
                        'next': 'sneak'
                    }
                }
            },
            'around_forest': {
                'text': 'You find a rocky path around the forest. It looks safer but longer.',
                'choices': {
                    '1': {
                        'text': 'Take the rocky path',
                        'next': 'rocky_path'
                    },
                    '2': {
                        'text': 'Go back to the forest entrance',
                        'next': 'adventure'
                    }
                }
            },
            'investigate': {
                'text': 'You discover a friendly talking owl who offers to guide you.',
                'choices': {
                    '1': {
                        'text': 'Accept the owl\'s help',
                        'next': 'owl_guide'
                    },
                    '2': {
                        'text': 'Politely decline and continue alone',
                        'next': 'alone'
                    }
                }
            },
            'sneak': {
                'text': 'You successfully sneak past whatever was making the sounds.',
                'choices': {
                    '1': {
                        'text': 'Continue forward',
                        'next': 'continue_forward'
                    }
                }
            },
            'rocky_path': {
                'text': 'The rocky path is difficult but safe. You reach a clearing with a beautiful lake.',
                'choices': {
                    '1': {
                        'text': 'Rest by the lake',
                        'next': 'lake_rest'
                    },
                    '2': {
                        'text': 'Continue past the lake',
                        'next': 'past_lake'
                    }
                }
            },
            'owl_guide': {
                'text': 'The owl leads you safely through the forest to a magical clearing. You win!',
                'choices': {}
            },
            'alone': {
                'text': 'You continue alone and get lost in the forest. Game over!',
                'choices': {}
            },
            'continue_forward': {
                'text': 'You find a treasure chest! You win!',
                'choices': {}
            },
            'lake_rest': {
                'text': 'You rest by the lake and discover a hidden cave entrance. You win!',
                'choices': {}
            },
            'past_lake': {
                'text': 'You continue past the lake and find a village. You win!',
                'choices': {}
            }
        }
    
    def play_story(self, story_key='adventure'):
        """Play an interactive story"""
        current_scene = story_key
        
        print(f"\n🎭 {self.stories[story_key]['title']}")
        print("=" * 50)
        
        while current_scene in self.stories:
            scene = self.stories[current_scene]
            
            # Display scene text
            if 'start' in scene:
                print(f"\n{scene['start']}")
            elif 'text' in scene:
                print(f"\n{scene['text']}")
            
            # Check if story ends
            if not scene.get('choices'):
                print("\n🎉 The End!")
                break
            
            # Display choices
            print("\nWhat do you do?")
            for key, choice in scene['choices'].items():
                print(f"{key}. {choice['text']}")
            
            # Get user choice
            while True:
                choice = input("\nEnter your choice: ").strip()
                if choice in scene['choices']:
                    current_scene = scene['choices'][choice]['next']
                    break
                else:
                    print("Invalid choice! Please try again.")
    
    def create_custom_story(self):
        """Allow user to create a custom story"""
        print("Create Your Own Story!")
        print("=" * 30)
        
        title = input("Enter story title: ")
        start_text = input("Enter starting text: ")
        
        story = {
            'title': title,
            'start': start_text,
            'choices': {}
        }
        
        print("Add choices (enter 'done' when finished):")
        choice_num = 1
        
        while True:
            choice_text = input(f"Choice {choice_num} text (or 'done'): ")
            if choice_text.lower() == 'done':
                break
            
            next_scene = input(f"Next scene key for choice {choice_num}: ")
            
            story['choices'][str(choice_num)] = {
                'text': choice_text,
                'next': next_scene
            }
            choice_num += 1
        
        print(f"\nStory '{title}' created!")
        return story
    
    def run_story_generator(self):
        """Run the story generator application"""
        print("Welcome to the Interactive Story Generator!")
        print("=" * 50)
        
        while True:
            print("\nOptions:")
            print("1. Play 'The Mysterious Forest'")
            print("2. Create custom story")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                self.play_story('adventure')
            
            elif choice == '2':
                custom_story = self.create_custom_story()
                play_custom = input("Would you like to play your custom story? (y/n): ").lower()
                if play_custom == 'y':
                    # This would require more complex story management
                    print("Custom story playing not implemented in this demo.")
            
            elif choice == '3':
                print("Goodbye! 📚")
                break
            
            else:
                print("Invalid choice! Please enter 1-3.")

# Demo the story generator
story_gen = StoryGenerator()
print("Story Generator Demo:")
story_gen.run_story_generator()

print("\n=== ALL CREATIVE PROJECTS COMPLETED ===")
print("These creative applications demonstrate:")
print("• ASCII art and text manipulation")
print("• Color and styling in terminal")
print("• Animation and visual effects")
print("• Interactive storytelling")
print("• User interface design")
print("• Creative programming concepts")
print("\nThese projects show how Python can be used for fun and creative purposes!")
