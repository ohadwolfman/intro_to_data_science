##  The code isn't complete

from bs4 import BeautifulSoup as bs, BeautifulSoup
import urllib.request
import requests
import re  # for find by specific word instead full string

# load the web page content
r = requests.get("https://www.shufersal.co.il/online/he/A")

# convert to BeautifulSoup object
soup = bs(r.content, features="lxml")

# print the html and prettify it by reorder the lines to their levels
soup.prettify()

# go to the supermarket area
market = soup.find(class_="secondMenu resizable menuJS hiddenChildren")

# grab all the links from market
links_eatable = market.find_all("a")
all_links = [i["href"] for i in links_eatable]


# we found out that every link which has less than 14 digits is irrelevant
def links_list(lst):
    links = []
    for link in lst:
        if len(link) >= 14:
            links.append(link)
    return links


def get_html_into_soup(string):
    html = urllib.request.urlopen(string)
    soupy = BeautifulSoup(html, features="lxml")
    return soupy


def data_food(link):
    link2 = urllib.request.urlopen(link)
    food = link2.select("li#data-food")
    return food
