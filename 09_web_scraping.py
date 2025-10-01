# ===========================================
# WEB SCRAPING - Extracting Data from Websites
# ===========================================

print("=== WEB SCRAPING BASICS ===")

# IMPORTANT NOTE: Always respect robots.txt and website terms of service
# Only scrape websites that allow it and don't overload servers

# BASIC WEB SCRAPING WITH REQUESTS AND BEAUTIFULSOUP
print("\n--- Basic Web Scraping Setup ---")

# First, install required packages:
# pip install requests beautifulsoup4 lxml

import requests
from bs4 import BeautifulSoup
import time
import json

# BASIC HTTP REQUESTS
print("\n--- Making HTTP Requests ---")

def make_simple_request(url):
    """Make a simple HTTP GET request"""
    try:
        # Send GET request
        response = requests.get(url)
        
        # Check if request was successful
        response.raise_for_status()  # Raises exception for bad status codes
        
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers.get('Content-Type', 'Unknown')}")
        print(f"Content Length: {len(response.content)} bytes")
        
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

# Test with a simple website
# Note: We'll use example.com which is safe for testing
test_url = "https://httpbin.org/html"  # A test service that returns HTML
response = make_simple_request(test_url)

# PARSING HTML WITH BEAUTIFULSOUP
print("\n--- Parsing HTML ---")

def parse_html_demo():
    """Demonstrate HTML parsing with BeautifulSoup"""
    
    # Sample HTML content (in real scraping, this comes from requests)
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sample Web Page</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Welcome to Our Website</h1>
        <div class="container">
            <p class="intro">This is a sample paragraph.</p>
            <ul id="menu">
                <li><a href="/home">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
            <div class="content">
                <h2>News Section</h2>
                <article class="news-item">
                    <h3>Breaking News</h3>
                    <p>This is the latest news article.</p>
                    <span class="date">2024-01-15</span>
                </article>
                <article class="news-item">
                    <h3>Technology Update</h3>
                    <p>Latest technology developments.</p>
                    <span class="date">2024-01-14</span>
                </article>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.find('title').text
    print(f"Page Title: {title}")
    
    # Extract main heading
    h1 = soup.find('h1').text
    print(f"Main Heading: {h1}")
    
    # Extract all paragraphs
    paragraphs = soup.find_all('p')
    print(f"Found {len(paragraphs)} paragraphs:")
    for i, p in enumerate(paragraphs, 1):
        print(f"  {i}. {p.text}")
    
    # Extract navigation menu
    menu = soup.find('ul', id='menu')
    if menu:
        links = menu.find_all('a')
        print(f"\nNavigation Menu:")
        for link in links:
            print(f"  - {link.text}: {link.get('href')}")
    
    # Extract news articles
    articles = soup.find_all('article', class_='news-item')
    print(f"\nFound {len(articles)} news articles:")
    for i, article in enumerate(articles, 1):
        title = article.find('h3').text
        date = article.find('span', class_='date').text
        print(f"  {i}. {title} ({date})")
    
    return soup

# Run the HTML parsing demo
soup = parse_html_demo()

# SCRAPING REAL WEBSITE DATA
print("\n--- Scraping Real Website Data ---")

def scrape_quote_website():
    """Scrape quotes from a sample quotes website"""
    
    # For demonstration, we'll create a mock response
    # In real scraping, you would use: response = requests.get(url)
    
    mock_html = """
    <html>
    <body>
        <div class="quotes">
            <div class="quote">
                <p class="text">The only way to do great work is to love what you do.</p>
                <span class="author">Steve Jobs</span>
                <div class="tags">
                    <span class="tag">work</span>
                    <span class="tag">passion</span>
                    <span class="tag">success</span>
                </div>
            </div>
            <div class="quote">
                <p class="text">Innovation distinguishes between a leader and a follower.</p>
                <span class="author">Steve Jobs</span>
                <div class="tags">
                    <span class="tag">innovation</span>
                    <span class="tag">leadership</span>
                </div>
            </div>
            <div class="quote">
                <p class="text">Life is what happens to you while you're busy making other plans.</p>
                <span class="author">John Lennon</span>
                <div class="tags">
                    <span class="tag">life</span>
                    <span class="tag">philosophy</span>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(mock_html, 'html.parser')
    quotes = []
    
    # Find all quote elements
    quote_elements = soup.find_all('div', class_='quote')
    
    for quote_elem in quote_elements:
        # Extract quote text
        text = quote_elem.find('p', class_='text').text
        
        # Extract author
        author = quote_elem.find('span', class_='author').text
        
        # Extract tags
        tag_elements = quote_elem.find_all('span', class_='tag')
        tags = [tag.text for tag in tag_elements]
        
        # Create quote dictionary
        quote = {
            'text': text,
            'author': author,
            'tags': tags
        }
        
        quotes.append(quote)
    
    return quotes

# Scrape quotes
quotes = scrape_quote_website()
print(f"Scraped {len(quotes)} quotes:")
for i, quote in enumerate(quotes, 1):
    print(f"\n{i}. \"{quote['text']}\"")
    print(f"   - {quote['author']}")
    print(f"   - Tags: {', '.join(quote['tags'])}")

# SAVING SCRAPED DATA
print("\n--- Saving Scraped Data ---")

def save_quotes_to_file(quotes, filename='quotes.json'):
    """Save scraped quotes to a JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(quotes, file, indent=2, ensure_ascii=False)
        print(f"Quotes saved to {filename}")
    except Exception as e:
        print(f"Error saving quotes: {e}")

def save_quotes_to_csv(quotes, filename='quotes.csv'):
    """Save scraped quotes to a CSV file"""
    try:
        import csv
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Author', 'Tags'])  # Header
            
            for quote in quotes:
                writer.writerow([
                    quote['text'],
                    quote['author'],
                    ', '.join(quote['tags'])
                ])
        print(f"Quotes saved to {filename}")
    except Exception as e:
        print(f"Error saving quotes to CSV: {e}")

# Save the scraped data
save_quotes_to_file(quotes)
save_quotes_to_csv(quotes)

# ADVANCED SCRAPING TECHNIQUES
print("\n--- Advanced Scraping Techniques ---")

def advanced_scraping_demo():
    """Demonstrate advanced scraping techniques"""
    
    # Sample HTML with more complex structure
    complex_html = """
    <html>
    <body>
        <div class="products">
            <div class="product" data-id="1" data-price="29.99">
                <img src="/images/product1.jpg" alt="Product 1">
                <h3>Wireless Headphones</h3>
                <p class="description">High-quality wireless headphones with noise cancellation.</p>
                <div class="rating" data-rating="4.5">★★★★☆</div>
                <span class="price">$29.99</span>
                <button class="add-to-cart">Add to Cart</button>
            </div>
            <div class="product" data-id="2" data-price="49.99">
                <img src="/images/product2.jpg" alt="Product 2">
                <h3>Smart Watch</h3>
                <p class="description">Fitness tracking and smart notifications.</p>
                <div class="rating" data-rating="4.2">★★★★☆</div>
                <span class="price">$49.99</span>
                <button class="add-to-cart">Add to Cart</button>
            </div>
        </div>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(complex_html, 'html.parser')
    products = []
    
    # Find all product elements
    product_elements = soup.find_all('div', class_='product')
    
    for product_elem in product_elements:
        # Extract data attributes
        product_id = product_elem.get('data-id')
        price = float(product_elem.get('data-price'))
        
        # Extract text content
        name = product_elem.find('h3').text
        description = product_elem.find('p', class_='description').text
        
        # Extract image source
        img = product_elem.find('img')
        image_url = img.get('src') if img else None
        
        # Extract rating
        rating_elem = product_elem.find('div', class_='rating')
        rating = float(rating_elem.get('data-rating')) if rating_elem else None
        
        # Create product dictionary
        product = {
            'id': product_id,
            'name': name,
            'description': description,
            'price': price,
            'image_url': image_url,
            'rating': rating
        }
        
        products.append(product)
    
    return products

# Scrape products
products = advanced_scraping_demo()
print(f"Scraped {len(products)} products:")
for product in products:
    print(f"\nProduct ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']}")
    print(f"Rating: {product['rating']}/5")
    print(f"Description: {product['description']}")

# HANDLING DYNAMIC CONTENT
print("\n--- Handling Dynamic Content ---")

def scrape_with_selenium_demo():
    """
    Demonstrate scraping dynamic content with Selenium
    Note: This is a conceptual example - Selenium needs to be installed
    """
    
    # Install Selenium: pip install selenium
    # Download ChromeDriver and add to PATH
    
    selenium_code_example = """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Set up Chrome driver
    driver = webdriver.Chrome()
    
    try:
        # Navigate to page
        driver.get('https://example.com')
        
        # Wait for element to load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dynamic-content"))
        )
        
        # Extract data
        data = element.text
        
        # Click buttons, fill forms, etc.
        button = driver.find_element(By.CSS_SELECTOR, '.load-more')
        button.click()
        
        # Wait for new content to load
        time.sleep(2)
        
        # Extract updated content
        updated_data = driver.find_element(By.ID, "content").text
        
    finally:
        driver.quit()
    """
    
    print("Selenium example code (conceptual):")
    print(selenium_code_example)

scrape_with_selenium_demo()

# RESPECTFUL SCRAPING
print("\n--- Respectful Scraping Practices ---")

def respectful_scraper(url, delay=1):
    """Example of respectful scraping with delays and headers"""
    
    # Set up headers to identify our scraper
    headers = {
        'User-Agent': 'Educational Scraper (Learning Python)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    try:
        # Make request with headers
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Add delay to be respectful
        time.sleep(delay)
        
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

print("Respectful scraping guidelines:")
print("1. Check robots.txt file")
print("2. Add delays between requests")
print("3. Use proper User-Agent headers")
print("4. Respect rate limits")
print("5. Don't overload servers")
print("6. Follow website terms of service")

# WEB SCRAPING PROJECT: NEWS HEADLINES SCRAPER
print("\n--- Project: News Headlines Scraper ---")

class NewsScraper:
    """A simple news scraper"""
    
    def __init__(self):
        self.articles = []
    
    def scrape_news_headlines(self):
        """Scrape news headlines (mock data for demonstration)"""
        
        # Mock HTML content
        news_html = """
        <html>
        <body>
            <div class="news-container">
                <article class="news-item">
                    <h2 class="headline">Python 3.12 Released with Performance Improvements</h2>
                    <p class="summary">The latest version of Python includes significant performance enhancements.</p>
                    <span class="date">2024-01-15</span>
                    <span class="category">Technology</span>
                </article>
                <article class="news-item">
                    <h2 class="headline">Scientists Discover New Exoplanet</h2>
                    <p class="summary">A potentially habitable planet has been found in a nearby star system.</p>
                    <span class="date">2024-01-14</span>
                    <span class="category">Science</span>
                </article>
                <article class="news-item">
                    <h2 class="headline">Renewable Energy Reaches New Milestone</h2>
                    <p class="summary">Solar and wind power now account for over 30% of global electricity.</p>
                    <span class="date">2024-01-13</span>
                    <span class="category">Environment</span>
                </article>
            </div>
        </body>
        </html>
        """
        
        soup = BeautifulSoup(news_html, 'html.parser')
        articles = soup.find_all('article', class_='news-item')
        
        for article in articles:
            headline = article.find('h2', class_='headline').text
            summary = article.find('p', class_='summary').text
            date = article.find('span', class_='date').text
            category = article.find('span', class_='category').text
            
            article_data = {
                'headline': headline,
                'summary': summary,
                'date': date,
                'category': category
            }
            
            self.articles.append(article_data)
    
    def filter_by_category(self, category):
        """Filter articles by category"""
        return [article for article in self.articles if article['category'] == category]
    
    def search_headlines(self, keyword):
        """Search headlines for a keyword"""
        keyword_lower = keyword.lower()
        return [article for article in self.articles if keyword_lower in article['headline'].lower()]
    
    def save_to_file(self, filename='news_articles.json'):
        """Save articles to JSON file"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.articles, file, indent=2, ensure_ascii=False)
            print(f"Articles saved to {filename}")
        except Exception as e:
            print(f"Error saving articles: {e}")
    
    def display_articles(self):
        """Display all articles"""
        print(f"\nFound {len(self.articles)} articles:")
        for i, article in enumerate(self.articles, 1):
            print(f"\n{i}. {article['headline']}")
            print(f"   Category: {article['category']}")
            print(f"   Date: {article['date']}")
            print(f"   Summary: {article['summary']}")

# Use the news scraper
scraper = NewsScraper()
scraper.scrape_news_headlines()
scraper.display_articles()

# Filter by category
tech_articles = scraper.filter_by_category('Technology')
print(f"\nTechnology articles: {len(tech_articles)}")

# Search for keyword
python_articles = scraper.search_headlines('Python')
print(f"Articles mentioning 'Python': {len(python_articles)}")

# Save to file
scraper.save_to_file()

# BEST PRACTICES SUMMARY
print("\n=== WEB SCRAPING BEST PRACTICES ===")
print("1. Always check robots.txt before scraping")
print("2. Respect rate limits and add delays")
print("3. Use proper User-Agent headers")
print("4. Handle errors gracefully")
print("5. Cache data to avoid repeated requests")
print("6. Follow website terms of service")
print("7. Consider using APIs when available")
print("8. Test with small amounts of data first")
print("9. Be mindful of copyright and legal issues")
print("10. Use appropriate tools for the job (requests + BeautifulSoup vs Selenium)")

print("\n=== Web Scraping Examples Complete ===")
print("Remember: Always scrape responsibly and legally!")
