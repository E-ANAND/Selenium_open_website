

# web_scraping.py

# Importing Necessary Files

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Chrome Driver Installation
 
driver = webdriver.Chrome(ChromeDriverManager().install())

# Website to get the data

website = "https://www.msn.com/en-in/"

driver.get(website)

driver.quit()
