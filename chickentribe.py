import json
import random
import time
import logging
import sys
import os
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import psutil


LOG_FILE = 'chickentribe/logfile.log'
FILE_ADDRESS = 'chickentribe/address.html'
FILE_TIME = 'chickentribe/time.html'


def setup_logger(log_file_path, logger_name='MyAppLogger'):
    logger = logging.getLogger(logger_name)
    logger.handlers = []
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def kill_chrome_and_chromedriver(logger):
    for proc in psutil.process_iter():
        if 'chrome' in proc.name().lower() or 'chromedriver' in proc.name().lower():
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


def driversetup(logger):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=selenium")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("lang=en-US")
    options.add_argument("location=US")
    options.add_argument(f"--window-size={1920},{1080}")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.page_load_strategy = 'normal'
    # options.binary_location = '/usr/bin/google-chrome'

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    ]
    selected_user_agent = random.choice(user_agents)
    options.add_argument(f"user-agent={selected_user_agent}")

    caps = webdriver.DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.google.com/"}})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver

def random_sleep(min_seconds, max_seconds):
    time.sleep(random.uniform(min_seconds, max_seconds))

def simulate_human_interaction(driver, logger):
    action = ActionChains(driver)
    body_element = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(random.randint(1, 3)):
        action.send_keys_to_element(body_element, Keys.PAGE_DOWN).perform()
        random_sleep(0.5, 1.0)
        action.send_keys_to_element(body_element, Keys.PAGE_UP).perform()
        random_sleep(0.5, 1.0)
    action.move_to_element(body_element).perform()
    random_sleep(0.5, 1.0)
    action.move_by_offset(random.randint(0, 100), random.randint(0, 100)).perform()
    random_sleep(0.5, 1.0)


def extract_owner_address_from_file(file_path, logger):
    try:
        with open(FILE_ADDRESS, 'r') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.find_all("table")

        for table in tables:
            if table.find("th", {"title": "Owner"}):
                visible_rows = table.select("tbody tr:not(.ant-table-measure-row)")
                if visible_rows:
                    owner_address_element = visible_rows[0].select_one("td:nth-of-type(2) a")
                    if owner_address_element:
                        address = owner_address_element.text.strip()
                        logger.info(f"Owner address found: {address}")
                        return address
                    else:
                        logger.info("Owner address not found in the table.")
                        return "Address not found"
                else:
                    logger.info("No visible rows found in the owner table.")
                    return "No rows in table"
    except Exception as e:
        logger.info(f"Error while extracting owner address: {e}")
        return f"Error: {e}"


def extract_time_from_file(file_path, logger):
    try:
        with open(file_path, 'r') as file:
            html_content = file.read()
        logger.info(f"Successfully read HTML content from '{file_path}'.")

        soup = BeautifulSoup(html_content, 'html.parser')
        time_column_index = 4

        table = soup.select_one("#rc-tabs-0-panel-txs table")
        if not table:
            logger.info("The specific table with ID 'rc-tabs-0-panel-txs' was not found.")
            return "Table not found"

        time_cell = table.select_one("tbody tr:nth-of-type(2) td:nth-of-type(4)")
        if not time_cell:
            logger.info("Time cell not found in the specified row and column.")
            return "Time cell not found"

        hold_time = time_cell.text.strip()
        logger.info(f"Time successfully extracted: {hold_time}")
        return hold_time

    except Exception as e:
        logger.info(f"An unexpected error occurred while extracting time from '{file_path}': {e}")
        return f"Error: {e}"


def getholderaddress(url_holder, driver, logger):

    try:

        driver.get(url_holder)

        wait = WebDriverWait(driver, timeout=30)
        root = driver.find_element(By.ID, 'root')
        body = driver.find_element(By.TAG_NAME, 'body')

        wait.until(lambda d: driver.execute_script('return document.readyState') == 'complete')
        wait.until(lambda d: root.is_displayed())
        wait.until(lambda d: body.is_displayed())

        random_sleep(7, 8)

        simulate_human_interaction(driver, logger)

        root_html = driver.find_element(By.ID, 'root').get_attribute('outerHTML')
        with open(FILE_ADDRESS, 'w') as file:
            file.write(root_html)

        solana_address = extract_owner_address_from_file(FILE_ADDRESS, logger)
        logger.info(f"Holder Address: {solana_address}")

    except TimeoutException:
        logger.error("Timed out waiting for page to load")
        solana_address = "Error: Page did not load properly"
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        solana_address = "Error: Unexpected issue occurred"
    return solana_address


def get_hold_time(url_time, driver, logger):
    try:

        driver.get(url_time)

        wait = WebDriverWait(driver, timeout=30)
        root = driver.find_element(By.ID, 'root')
        body = driver.find_element(By.TAG_NAME, 'body')

        wait.until(lambda d: driver.execute_script('return document.readyState') == 'complete')
        wait.until(lambda d: root.is_displayed())
        wait.until(lambda d: body.is_displayed())

        random_sleep(8, 9)

        simulate_human_interaction(driver, logger)

        javascript = """
        var elements = document.querySelectorAll('span.sc-kDvujY.dxDyul');
        var targetElement = null;
        var count = 0;

        for (var i = 0; i < elements.length; i++) {
            if (elements[i].textContent.includes('Time')) {
                count++;
                if (count === 2) {
                    targetElement = elements[i];
                    break;
                }
            }
        }

        if (!targetElement) {
            // Second element not found, so select the first
            for (var i = 0; i < elements.length; i++) {
                if (elements[i].textContent.includes('Time')) {
                    targetElement = elements[i];
                    break;
                }
            }
        }

        if (targetElement) {
            targetElement.click();
        } else {
            console.log('Element with "Time" not found');
        }
        """

        try:
            driver.execute_script(javascript)
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        time.sleep(2)

        body_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')

        with open(FILE_TIME, 'w') as file:
            file.write(body_html)

        hold_time = extract_time_from_file(FILE_TIME, logger)
        logger.info(f"Hold time extracted: {hold_time}")

    except TimeoutException as e:
        logger.info(f"TimeoutException encountered: {e}. The website might be unresponsive or the element locators might be incorrect.")
        hold_time = "Error: Timed out"
    except Exception as e:
        logger.info(f"Unexpected error encountered: {e}. Review the stack trace for details and check the website's structure.")
        hold_time = "Error: Unexpected issue occurred"
    finally:
        logger.info("Closing the web driver...")
        driver.close()
        logger.info("Web driver closed for time.")

    return hold_time


def process_item(item, driver, logger):
    account = item.get('account')
    if not account:
        logger.info("Account information not found in the item.")
        return

    time.sleep(1)
    url_holder = f"https://solscan.io/token/{account}#holders"
    logger.info(f"https://solscan.io/token/{account}#holders")
    time.sleep(1)
    url_time = f"https://solscan.io/token/{account}#txs"
    logger.info(f"https://solscan.io/token/{account}#txs")
    time.sleep(1)

    try:
        solana_address = getholderaddress(url_holder, driver, logger)
        hold_time = get_hold_time(url_time, driver, logger)
        update_json_data(item, solana_address, hold_time, logger)
        logger.info(f"Successfully processed account {account}.")
    except Exception as e:
        logger.error(f"Error processing {account}: {e}")


def update_json_data(item, solana_address, hold_time_str, logger):

    hold_time_format = "%m-%d-%Y %H:%M:%S"
    hold_time = datetime.strptime(hold_time_str, hold_time_format)

    current_time = datetime.now()
    hold_time_unix = int(hold_time.timestamp())
    current_time_unix = int(current_time.timestamp())

    item['holder data'] = [
        {"holder": solana_address},
        {"when acquired": hold_time_unix},
        {"time checked": current_time_unix}
    ]


def find_start_index(nft_metadata, processed_indices, logger):
    for index, item in enumerate(nft_metadata):
        if index in processed_indices:
            continue
        if 'holder data' not in item:
            logger.info(f"Starting from index {index}: No 'holder data' field found.")
            return index

    logger.info("All items have 'holder data'. Moving to the next priority.")

    for index, item in enumerate(nft_metadata):
        if index in processed_indices:
            continue
        if 'holder data' in item:
            holder = item['holder data'][0]['holder']
            if holder is None:
                logger.info(f"Starting from index {index}: Found invalid 'holder' value.")
                return index
            if len(holder) not in range(32, 45) and holder != "Magic Eden V2 Authority":
                logger.info(f"Starting from index {index}: Found invalid 'holder' value.")
                return index

    logger.info("All items have valid 'holder' values. Moving to the next priority.")

    for index, item in enumerate(nft_metadata):
        if index in processed_indices:
            continue
        if 'holder data' in item:
            when_acquired = item['holder data'][1]['when acquired']
            if not isinstance(when_acquired, int):
                logger.info(f"Starting from index {index}: 'when acquired' is not a Unix epoch timestamp.")
                return index

    logger.info("All items have valid 'when acquired' timestamps. Moving to the next priority.")

    oldest_index = None
    oldest_time = float('inf')
    for index, item in enumerate(nft_metadata):
        if index in processed_indices:
            continue
        if 'holder data' in item:
            time_checked = item['holder data'][2]['time checked']
            if time_checked < oldest_time:
                oldest_time = time_checked
                oldest_index = index

    if oldest_index is not None:
        logger.info(f"Starting from index {oldest_index}: It has the oldest 'time checked'.")
        return oldest_index
    else:
        logger.info("No items to prioritize based on 'time checked'.")
        return len(nft_metadata)


def get_next_item_index(nft_metadata, logger):
    return find_start_index(nft_metadata, logger)

def main():
    logger = setup_logger(LOG_FILE)

    logger.info("Starting new run. Appending to the existing logfile.")

    kill_chrome_and_chromedriver(logger)

    processed_data_file = 'chickentribe/with_rarity_and_holder_data.json'
    if os.path.exists(processed_data_file):
        try:
            with open(processed_data_file, 'r') as file:
                nft_metadata = json.load(file)
            logger.info("Continuing from previously saved progress.")
        except Exception as e:
            logger.error(f"Error loading processed data: {e}")
            return
    else:
        try:
            with open('chickentribe/with_rarity.json', 'r') as file:
                nft_metadata = json.load(file)
                logger.info("Starting from the beginning as no progress file found.")
        except Exception as e:
            logger.error(f"Error loading initial data: {e}")
            return

    processed_count = 0
    processed_indices = set()
    while processed_count < 100:
        next_index = find_start_index(nft_metadata, processed_indices, logger)
        if next_index >= len(nft_metadata):
            logger.info("All items have been processed or no more items to prioritize.")
            break

        item = nft_metadata[next_index]
        logger.info(f"Processing item {processed_count + 1}/100 with account: {item.get('account', 'Unknown')} (Global index: {next_index + 1}/{len(nft_metadata)})")
        driver = driversetup(logger)

        try:
            process_item(item, driver, logger)
            processed_count += 1
            processed_indices.add(next_index)
        except Exception as e:
            logger.error(f"Error processing item with account {item.get('account', 'Unknown')}: {e}")
        finally:
            driver.quit()
            logger.info(f"WebDriver closed for item {next_index + 1}")

    try:
        with open(processed_data_file, 'w') as file:
            json.dump(nft_metadata, file, indent=4)
            logger.info("Progress saved after processing 100 items.")
    except Exception as e:
        logger.error(f"An error occurred while saving the progress: {e}")

if __name__ == '__main__':
    main()
