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
links = []
for link in all_links:
    if len(link) >= 14:
        links.append(link)
print(links)


def get_html_into_soup(string):
    html = urllib.request.urlopen(string)
    soupy = BeautifulSoup(html, features="lxml")
    return soupy

#   links1 = soup.find("ul", attrs={"class":"socials"})
#    links = links1.find_all("a")
#    actual_links = [i['href'] for i in links]
#    print(actual_links)
