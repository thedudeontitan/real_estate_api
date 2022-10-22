from scrapers.rf import fs_data
from scrapers.a import ap_data
import threading
from scrapers.config import rf_city

if __name__ =="__main__":


    print("="*100)
    print("HELLO! THIS PROGRAM MAY TAKE QUITE SOME TIME TO SCRAPE THE DATA, YOU CAN MINIMIZE THIS WINDOW AND CONTINUE USING YOUR COMPUTER:)")
    print("="*100)
       
    t1 = threading.Thread(target=fs_data, args=(rf_city,))
    t2 = threading.Thread(target=ap_data, args=())
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("DONE! DATA HAS BEEN SCRAPED SUCCESSFULLY PLEASE CHECK 'For_Sale.csv' AND 'Rental.csv' FOR THE INFO!")

