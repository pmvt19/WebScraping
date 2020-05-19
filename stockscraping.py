import time
import requests
from bs4 import BeautifulSoup
import datetime

start = time.time()
timerHasBeenSetpip = False

def split(word):
    return [char for char in word]
now = time.time()
while(True):

    now = time.time()
    if now - start > 2:
        start = time.time()
        response = requests.get('https://markets.businessinsider.com/index/nasdaq_100')
        soup = BeautifulSoup(response.text, 'html.parser')
        el = soup.find_all(class_='push-data')
        currentDT = datetime.datetime.now()
        stockPrice = el[0].get_text()
        stockPrice = stockPrice.replace(",", "")
        value = str(currentDT) + "," + stockPrice + "\n"
        print(value)

        f = open("stockdata.csv", "a")
        f.write(value)
        f.close()