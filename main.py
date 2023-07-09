# example Link: https://www.aviationweather.gov/metar/data?ids=kunv
import requests
from bs4 import BeautifulSoup
import os

#Clear terminal
os.system("cls")

def scrape_metar(airport_id):
    URL = "https://www.aviationweather.gov/metar/data?ids=" + str(airport_id)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    section = soup.find(id="awc_main_content_wrap")
    section.find_all("code")
    return str(section.find("code").text)


def scrape_FFA_codes():

    #Much of code is derived from this stack overflow question
    #https://stackoverflow.com/questions/71492417/how-to-get-a-specific-columns-from-a-wiki-table
    
    from bs4 import BeautifulSoup
    airport_list = []
    URL = "https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"lxml")
    for items in soup.find(class_="wikitable").find_all("tr")[1:]:
        e = items.find_all('td')
        airport_list.append(str(e[3].text.strip()))
    
    return airport_list
        


def main():
    
    # metar = scrape_metar("kunv")
    # print (metar)
    # input("Press enter to exit")

    airport_codes = scrape_FFA_codes()
    print(len(airport_codes))
    print(airport_codes)



if __name__ == "__main__":
    main()