Take Webpage Screenshot with Python Selenium
Screenshots of webpages can be taken automatically with Python Selenium Web Driver. First load the selenium module and time module. You need the time module to wait for page loading to complete.

Then once the page is loaded, take the screenshot. This can be a png file or another image format. Then close the web browser, otherwise it will stay open indefinetly.

source:
```
https://pythonbasics.org/selenium-screenshot/
```

Example

Before you start, make sure that you have the Selenium Web Driver installed (unique for your Web Browser) and that you have the selenium module installed.

You can take a screenshot of a webpage with the method get_screenshot_as_file() with as parameter the filename.
The program below uses firefox to load a webpage and take a screenshot, but any web browser will do.

```
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")
```

The screenshot image will be stored in the same directory as your Python script. Unless you explicitly define the path where the screenshot has to be stored.

selenium screenshot

The first step is to import the required modules,

```
from selenium import webdriver
from time import sleep
Then fire up the browser and load a webpage.

driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)
```

When the page has loaded, you can take a screenshot using the method `.get_screenshot_as_file(filename)`.

```
driver.get_screenshot_as_file("screenshot.png")
```

Take screenshot of full page with Python Selenium

The above code only takes a screenshot of the visible browser window. There are several ways to take a full page screenshot, which includes the web page from top to bottom.
You can do it this way, note that it’s mandatory to set the browser to headless for this to work:

```
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://pythonbasics.org'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()
```