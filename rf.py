import re
from time import sleep
from random import randint
import csv
from scrape import get_html
from config import rf_city

def ap_data():
    re_home = r"/CA/[\w\s\-]+/[\w\s\-/]+/home/\d+"
    re_phone = r"phoneType\\\":\\\"Office\\\",\\\"twilioContactBoxPhone\\\":\\\"([\(\)\d\s-]+)\\"
    re_address = r"<div data-rf-test-id=\"abp-streetLine\" class=\"street-address font-weight-bold\" title=\"[\w\s]+\">([\w\s]+)<!-- -->,</div>"
    re_title = r"<div class=\"dp-subtext\" data-rf-test-id=\"abp-cityStateZip\">([\s\w,\-]+)<!-- -->, <!-- -->CA<!-- --> <!-- -->([\d]+)</div>"
    # re_zipcode = r"<span class=\"stateZipContainer\">\s*<span>(\w+)</span>\s*<span>(\d+)</span>\s*</span>"
    re_price = r"<div class=\"statsValue\">(<span class=\"\">)??(\$[\d\s,+]+)(</span>)??</div>"
    re_pages = r"<span class=\"pageText\" data-rf-test-name=\"download-and-save-page-number-text\">Viewing page \d+ of (\d+)</span>"
    re_agent = r"\"brokerageName\\\":\\\"Redfin\\\",\\\"fullName\\\":\\\"([\w\s]+)\\\""
    homes = []
    for city in rf_city:
        page_html = get_html(city)    
        pages = int(re.search(re_pages,page_html).group(1))
        # print("city: ",city)
        print("no of pages:",pages)
        

        for page in range(1,pages+1):
            sleep(randint(3,5))
            content = get_html(f'{city}/page-{page}')
            
            print("page no.: ",page)
            home_links = set(re.findall(re_home,content))
            for i in home_links:
                print(f"https://redfin.com{i}")
                homes.append(f"https://redfin.com{i}")

    f = open('For_Sale.csv','w')
    csvwriter = csv.writer(f) 
    fields = ['Address','Price','Zipcode','Agent/Owner','Phone No.'] 
    csvwriter.writerow(fields)

    data = []
    
    for i in homes:
        print(i)
        sleep(randint(3,5))
        house_html = get_html(i)

        try:
            address = re.search(re_address,house_html).group(1)+", "+re.search(re_title,house_html).group(1)
            print("address: ",address)
        except:
            address = "unknown"

        try:
            price = re.search(re_price,house_html).group(2)
            print("price: ",price)
        except:
            price = "unkown"

        try:
            zipcode = re.search(re_title,house_html).group(2)
            print("zipcode :",zipcode)
        except:
            zipcode = "unknown"

        try:
            agent_name = re.search(re_agent,house_html).group(2)
            print("agent name: :",agent_name)
        except:
            agent_name = "unknown"
        try:
            phone_no = re.search(re_phone,house_html).group(1)
            print("phone: ",phone_no)

        except:
            phone_no = "unknown"

        row = [address,price,zipcode,agent_name,phone_no]
        csvwriter.writerow(row)
    f.close()

ap_data()