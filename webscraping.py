import time
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import date

start = time.time()
timerHasBeenSetpip = False

def split(word):
    return [char for char in word]

now = time.time()
while(True):
    now = time.time()
    if now - start > 2:
        start = time.time()
        response = requests.get('https://www.google.com/search?q=temperature+in+plainfield&oq=temperature+in+plainfield&aqs=chrome.0.0l8.6848j1j7&sourceid=chrome&ie=UTF-8')
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = soup.find_all(class_='BNeawe iBp4i AP7Wnd')
        #wind = soup.find_all(class_='')

        print("", end = "\n")
        temperature = temp[1].get_text()
        value = ""

        temperature = split(temperature)

        for i in temperature:
            if i.isdigit():
                value = value + i



        #print(temp)
        #print(soup)
        #print(value)
        currentDT = datetime.datetime.now()
        #print(str(currentDT))

        toPrintToCSV = str(currentDT) + "," + value

        print(toPrintToCSV)


