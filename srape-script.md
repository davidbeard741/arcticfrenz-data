```PYTHON
import requests
from bs4 import BeautifulSoup
import json
import logging
from typing import Union, List, Dict

def scrape_site(url: str) -> Union[str, None]:
    """Scrapes the given website and returns the HTML content, or None if the scrape fails."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to scrape website: {url}, due to {str(e)}")
        return None

def parse_html(html: str) -> List[Dict[str, str]]:
    """Parses the given HTML content and returns a list of dictionaries of parsed data, or an empty list if the parsing fails."""
    soup = BeautifulSoup(html, "html.parser")
    results_container = soup.find(id="ResultsContainer")
    parsed_data = []
    
    if results_container:
        for result in results_container.find_all("div", class_="card-content"):
            title = result.find("h2", class_="title").text.strip() if result.find("h2", class_="title") else None
            company = result.find("h3", class_="company").text.strip() if result.find("h3", class_="company") else None
            location = result.find("p", class_="location").text.strip() if result.find("p", class_="location") else None
            parsed_data.append({"title": title, "company": company, "location": location})
    
    return parsed_data

def save_data(data: List[Dict[str, str]], filename: str) -> None:
    """Saves the given list of dictionaries of data to the given JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to '{filename}'.")
    except Exception as e:
        logging.error(f"Failed to save data to {filename}, due to {str(e)}")

def main():
    """Scrapes the website, parses the HTML, and saves the data."""
    url = "https://realpython.github.io/fake-jobs/"
    html = scrape_site(url)

    if html:
        parsed_data = parse_html(html)
        if parsed_data:
            save_data(parsed_data, "arcticfrenz.json")
        else:
            logging.error(f"Failed to parse HTML from {url}")
    else:
        logging.error(f"Failed to scrape website: {url}")

if __name__ == "__main__":
    main()
```