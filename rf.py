import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys,os
from random import randint
import csv
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()
def rf_data(url):
    re_home = r"https://www.redfin.com/city/\d+/CA/[\w-]+"
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={os.path.join(os.getcwd(),'Selenium')}") 

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    sleep(randint(2,5))
    driver.get(url)

    content = driver.page_source
    # sleep(50)
    with open('__pycache__/rf.html','w') as f:
        f.write("\n".join(set(re.findall(re_home,content))))

rf_data("https://www.redfin.com/state/California")