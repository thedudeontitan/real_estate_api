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
import requests
import pandas as pd

from scrape import get_html

chromedriver_autoinstaller.install()

def ap_data():
    re_home = r"https://www\.apartments\.com/[\w-]+/[\w]{7}/"
    re_phone = r"<a class=\"[\w\s-]+\" href=\"tel:([\d]+)\">"
    re_name = r"<span class=\"js-placardTitle title\">([\w\s-]+)</span>"
    re_address = r"<div class=\"property-address js-url\" title=\"(.+) \d{5}\">"
    re_title = r"<title>\s*([\w\s]*)-\s*([\w\s,]*)\| Apartments\.com</title>"
    re_zipcode = r"<div class=\"property-address js-url\" title=\".+ (\d{5})\">"
    
    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    sleep(randint(2,5))
    driver.get('https://www.apartments.com/ca')
    
    temp = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"pageRange"))) 
    pages = int(re.search(r"Page \d of (\d+)",temp.text).group(1))
    print(pages)
    homes = []

    f = open('rental.csv','w')
    csvwriter = csv.writer(f) 
    fields = ['Property Name','Address','Zipcode','Agent/Owner','Phone No.'] 
    csvwriter.writerow(fields)


    for page in range(1,2):
        sleep(randint(3,5))
        driver.get(f'https://www.apartments.com/ca/{page}/')
        print(page)
        content = driver.page_source
        # try:
        phone_no = re.search(re_phone,content).group(1)
        # except:
        #     phone_no = "unknown"

        # try:
        name = re.search(re_name,content).group(1)
        # except:
        #     name = "unknown"

        # try:
        address = re.search(re_address,content).group(1)
        # except:
        #     address = "unknown"

        # try:
        zipcode = re.search(re_zipcode,content).group(1)
        # except:
        #     zipcode = "unknown"
        agent_name = "unknown"
        print(phone_no)
        print(name)
        print(address)
        print(zipcode)
        row = [name,address,zipcode,agent_name,phone_no]
        csvwriter.writerow(row)

    f.close()
    driver.close()
        
ap_data()