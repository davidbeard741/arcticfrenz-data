import requests
from bs4 import BeautifulSoup
import json

def scrape_site():
    url = "https://httpbin.org/html"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extracting data - example, extracting the first h1 text
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
        print("Failed to retrieve data from the website.")

if __name__ == "__main__":
    main()