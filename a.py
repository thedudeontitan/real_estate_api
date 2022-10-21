import re
from time import sleep
import sys,os
from random import randint
import csv
import requests

from scrape import get_html


def ap_data():
    re_home = r"https://www\.apartments\.com/[\w-]+/[\w]{7}/"
    re_phone = r"<a href=\"tel:(\d+)\">"
    re_name = r"<span class=\"js-placardTitle title\">([\w\s-]+)</span>"
    re_address = r"<div class=\"property-address js-url\" title=\"(.+) (\d{5})\">"
    re_title = r"<title>\s*([\w\s-]*)-\s*([\w\s,]*)\| Apartments\.com</title>"
    re_zipcode = r"<span class=\"stateZipContainer\">\s*<span>(\w+)</span>\s*<span>(\d+)</span>\s*</span>"
    re_price = r"<p class=\"rentInfoDetail\">([\$\d\s,-]+)</p>"
    re_pages = r"<span class=\"pageRange\">Page \d+ of (\d+)</span>"
    
    ca_html = get_html('https://www.apartments.com/ca')
    
    pages = int(re.search(re_pages,ca_html).group(1))
    print(pages)
    homes = []


    for page in range(1,pages):
        sleep(randint(3,5))
        content = get_html(f'https://www.apartments.com/ca/{page}/')
        print(page)
        home_links = set(re.findall(re_home,content))
        for i in home_links:
            homes.append(i)


    f = open('rental.csv','w')
    csvwriter = csv.writer(f) 
    fields = ['Property Name','Rental Price','Address','Zipcode','Agent/Owner','Phone No.'] 
    csvwriter.writerow(fields)

    data = []
    
    for i in homes:
        print(i)
        sleep(randint(3,5))
        house_html = get_html(i)


        try:
            name = re.search(re_title,house_html).group(1)
        except:
            name = "unknown"
        try:
            price = re.search(re_price,house_html).group(1)
        except:
            price = "unkown"
        try:
            address = re.search(re_title,house_html).group(2)
        except:
            address = "unknown"

        try:
            zipcode = re.search(re_zipcode,house_html).group(2)
        except:
            zipcode = "unknown"
        agent_name = "unknown"
        try:
            phone_no = re.search(re_phone,house_html).group(1)
        except:
            phone_no = "unknown"

        row = [name,price,address,zipcode,agent_name,phone_no]
        csvwriter.writerow(row)
    f.close()
    # print(f"{phone_no}\n{name}\n{address}\n{pincode}")
    # print(name)
    # print(phone_no)
    # print(zipcode)
    # print(address)
        

    # data = requests.get(homes[1]).text
    
        


ap_data()