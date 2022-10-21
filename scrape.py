import requests 
import random
import selenium 
import re
from time import sleep
def get_html(url):
    re_home = r"https://www.redfin.com/city/\d+/CA/[\w-]+"
    
    UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )

    ua = UAS[random.randrange(len(UAS))]

    headers = {'user-agent': ua}
    data = requests.get(url,headers=headers).text
    sleep(5)
    return data
    # with open('ca.html','w') as f:
    #     # f.write("\n".join(set(re.findall(re_home,data))))
    #     f.write(data)

# get_url('https://www.apartments.com/garnet-creek-rocklin-ca/kxfykgb/')