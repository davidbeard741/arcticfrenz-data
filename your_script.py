import requests
from bs4 import BeautifulSoup
import json
from reppy.robots import Robots
from urllib.parse import urlparse

def is_allowed_by_robots_txt(url):
    # Parse the URL to extract the scheme and netloc
    parsed_url = urlparse(url)
    # Construct the URL for the robots.txt file
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    # Fetch and parse the robots.txt file
    robots = Robots.fetch(robots_url)
    # Check if the given URL is allowed by the robots.txt rules
    return robots.allowed(url, '*')

def scrape_site():
    # URL of the webpage you want to scrape
    url = "https://httpbin.org/html"
    
    # Check if scraping this URL is allowed by the robots.txt rules
    if not is_allowed_by_robots_txt(url):
        print("Scraping is disallowed by robots.txt")
        return None

    # Make an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Return the HTML content of the page
        return response.text
    else:
        # Return None if the request failed
        return None

def parse_html(html):
    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    # Extract the text of the first h1 tag
    h1_text = soup.h1.text.strip()
    # Return the extracted text in a dictionary
    return {"header": h1_text}

def save_data(data):
    # Filename for the output JSON file
    filename = "arcticfrenz.json"
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the data to the file in JSON format
        json.dump(data, file, indent=4)

def main():
    # Scrape the website
    html = scrape_site()
    # Check if scraping was successful
    if html:
        # Parse the HTML content
        parsed_data = parse_html(html)
        # Save the parsed data to a JSON file
        save_data(parsed_data)
        print("Data saved to 'arcticfrenz.json'.")
    else:
        # Print an error message if scraping failed
        print("Failed to retrieve data from the website or scraping disallowed by robots.txt.")

# Python's standard boilerplate to execute the main function
if __name__ == "__main__":
    main()