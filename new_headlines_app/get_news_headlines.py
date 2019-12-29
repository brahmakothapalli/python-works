# This program gets the headlines from the News 18 website

import requests
from bs4 import BeautifulSoup as bs

# get response from the web app
res = requests.get("https://www.news18.com/")

# parse the source code
soup = bs(res.content, "lxml")
main_story = soup.findAll("ul", {"class":"lead-mstory"})
headlines = main_story[0].findChildren("li", recursive=False)
for head in headlines:
    print(head.text)
    print("*"*100)
