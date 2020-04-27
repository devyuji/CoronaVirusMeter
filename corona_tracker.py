import requests as rr
from bs4 import BeautifulSoup

# Required Internet Connection

def world():
    try:
        req = rr.get("https://www.worldometers.info/coronavirus/")
        total_cases = BeautifulSoup(req.content,"html.parser")
        confirm_cases = total_cases.find_all(class_ ="maincounter-number")
        print(f"Coronavirus Cases:{confirm_cases[0].get_text()}")
        print(f"Recovered:{confirm_cases[2].get_text()}")
        print(f"Death:{confirm_cases[1].get_text()}")
        active_case = total_cases.find(class_="number-table-main")
        print(f"Actve Cases:\n{active_case.get_text()}")
    
    except:
        print("Turn on your Internet connection")
    

def India():
    try:
        req = rr.get("https://www.worldometers.info/coronavirus/country/india/")
        corona_data = BeautifulSoup(req.content,"html.parser")
        total_cases = corona_data.find(class_ = "maincounter-number")
        confirm_cases = total_cases.find("span")
        print(f"Coronavirus Cases:\n{confirm_cases.get_text()}\n")
        death = corona_data.find_all(class_ ="number-table")
        print(f"Recovered:\n{death[0].get_text()}\n\nDeath: {death[1].get_text()}")
        # another wesite to know about the Actve cases
        req1 = rr.get("https://www.mohfw.gov.in/")
        active_case = BeautifulSoup(req1.content,"html.parser")
        data = active_case.find(class_ = "bg-blue")
        ac = data.find("strong")
        print(f"\nActive Cases:\n{ac.get_text()}")
    except:
        print("Turn on your Internet connection")

# world()
user = input('World(W) or India(I)').lower()
if (user == 'w'):
    world()
elif(user == 'i'):
    India()
else:
    print('wrong input!')



