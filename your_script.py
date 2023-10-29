import requests
from bs4 import BeautifulSoup
import json
from reppy.robots import Robots
from urllib.parse import urlparse

def is_allowed_by_robots_txt(url):
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    robots = Robots.fetch(robots_url)
    return robots.allowed(url, '*')

def scrape_site():
    url = "https://httpbin.org/html"
    
    if not is_allowed_by_robots_txt(url):
        print("Scraping is disallowed by robots.txt")
        return None

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    h1_text = soup.h1.text.strip()
    return {"header": h1_text}

def save_data(data):
    filename = "arcticfrenz.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    html = scrape_site()
    if html:
        parsed_data = parse_html(html)
        save_data(parsed_data)
        print("Data saved to 'arcticfrenz.json'.")
    else:
        print("Failed to retrieve data from the website or scraping disallowed by robots.txt.")

if __name__ == "__main__":
    main()