import requests as rr
from bs4 import BeautifulSoup

# Required Internet Connection

def world():
    req = rr.get('https://www.worldometers.info/coronavirus/')
    data = BeautifulSoup(req.content, 'html.parser')
    keep = data.find_all(id='maincounter-wrap')
    active = data.find(class_="number-table-main")
    for i in range(len(keep)):
        print(keep[i].get_text(),end='')
    print(f"Active case:\n\n{active.get_text()}")

world()


