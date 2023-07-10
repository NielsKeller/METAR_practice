"""
METAR Practice
Author: Niels Keller
"""

# example Link: https://www.aviationweather.gov/metar/data?ids=kunv
import requests
from bs4 import BeautifulSoup
import os
import random



def scrape_metar(airport_id):
    """
    Scrapes METAR from https://www.aviationweather.gov/metar/data?ids=
    Pass in 4 letter airport code as airport_id.
    Returns "error" if unable to access site
    """

    URL = "https://www.aviationweather.gov/metar/data?ids=" + str(airport_id)
    try:
        page = requests.get(URL)
        metar_string = str(BeautifulSoup(page.content, "html.parser").find(id="awc_main_content_wrap").find("code").text) #Returns metar code as string
    except:
        return "error"
    return metar_string
    


def scrape_FFA_codes():
    """
    Returns a list of a ton of airport codes
    
    Much of code is derived from this stack overflow question
    https://stackoverflow.com/questions/71492417/how-to-get-a-specific-columns-from-a-wiki-table
    """
    
    airport_list = []
    URL = "https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States"
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"lxml")
    for items in soup.find(class_="wikitable").find_all("tr")[1:]:
        e = items.find_all('td')
        code = str(e[3].text.strip())
        if not(code == ""): #Some airports on the wiki lists have no code listed
            airport_list.append(code)
    return airport_list
        
#WIP ------------------------------------------------------------------

# # https://www.weather.gov/media/wrh/mesowest/metar_decode_key.pdf


# def decode_metar(airport_id):
#     """
#     Returns the decoded metar as string
#     """
#     URL = "https://en.wikipedia.org/wiki/List_of_airports_in_the_United_States"
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.text,"lxml")
#     for items in soup.find(class_="wikitable").find_all("tr")[1:]:
#         e = items.find_all('td')
#         code = str(e[3].text.strip())
#         if not(code == False): #Some airports on the wiki lists have no code listed
#             airport_list.append(code)
#     return airport_list


# def decode_metar(metar): # WIP as potental futre function
#     metar_list = metar.split()
#     metar_decoded_list = []

#     print(metar_list)

#     #first is always airport id
#     metar_decoded_list.append("Metar at airport" + metar_list[0])

#     #time of recording
#     metar_decoded_list.append("Time of recording:\nDay: " + metar_list[1][0:2]+"\nTime (zulu):"+metar_list[1][2:4]+":"+metar_list[1][4:6])

#     #next one can be Auto for automatic recording, or ommited
#     counter = 2 #counter so we can keep track if it was ommited or not
#     if metar_list[2] == "AUTO":
#         metar_decoded_list.append("Metar automaticly generated")
#         counter + 1

#     #winds
#     if len(metar_list[counter]) == 6:
#         #basic

#WIP end ------------------------------------------------------------------


def main():
    codes = scrape_FFA_codes()
    keep_going = True
    while keep_going == True:
        #Clear terminal
        os.system("cls")

        code = random.choice(codes)

        metar = scrape_metar(code)

        print(metar + "\n\n\nDecoded: https://e6bx.com/weather/"+code+"/?showDecoded=1&focuspoint=metardecoder\n\n\n\n")
                
        #Should the program keep going?
        user_input = input("Press enter to continue or type exit to exit: ")
        if user_input.lower() == "exit":
            keep_going = False



if __name__ == "__main__":
    main()