# Webpage Screenshot with Python and Selenium

A script for capturing screenshots of webpages automatically using Python and [Selenium](https://pythonbasics.org/selenium-screenshot/) WebDriver. The script supports capturing both visible viewport and full page screenshots.

Install the required Python modules:

```shell
pip install selenium
```

## Taking a Screenshot

To capture a screenshot, invoke the `get_screenshot_as_file()` method with the desired filename as the parameter. Below is an example that uses Firefox to load a webpage and take a screenshot. However, you can adapt the code to use any other web browser of your choice.

```python
from selenium import webdriver
from time import sleep

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get('https://www.python.org')

# Wait for the desired page to load
sleep(1)

# Capture and save the screenshot
driver.get_screenshot_as_file("screenshot.png")

# Close the browser
driver.quit()

print("Screenshot captured successfully!")
```

The screenshot will be saved in the same directory as the script, unless an alternative path is specified in the filename.

## Capturing Full Page Screenshot

To take a screenshot of the entire webpage (including off-screen parts), you may need to set the browser in headless mode and adjust the window size to the web page dimensions. The following code demonstrates how to do this with Chrome in headless mode:

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Target webpage URL
URL = 'https://pythonbasics.org'

driver.get(URL)

# Define a lambda to calculate the dimensions
S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)

# Set window size based on page dimensions (may require manual adjustment)
driver.set_window_size(S('Width'), S('Height'))

# Take full page screenshot and save
driver.find_element_by_tag_name('body').screenshot('full_web_screenshot.png')

# Close the browser
driver.quit()

print("Full page screenshot captured successfully!")
```