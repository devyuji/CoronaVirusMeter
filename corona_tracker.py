import requests as rr
from bs4 import BeautifulSoup

# Required Internet Connection

def data():
    req = rr.get('https://www.worldometers.info/coronavirus/')
    data = BeautifulSoup (req.content,'html.parser')
    keep = data.find_all(id ='maincounter-wrap')
    for i in range(len(keep)):
        print(keep[i].get_text(),end='')
data()