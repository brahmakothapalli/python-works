# importing the libraries
import requests
from bs4 import BeautifulSoup as bs

input_word = input("Enter the word: ")
url = "https://www.dictionary.com/browse/"+input_word+"?s=ts"
# it gets the source code of the web app
res = requests.get(url)
# print(res.text)
# lets parse the hrml source code using bs4
soup = bs(res.content, "lxml")
try:        
    pos = soup.findAll("span", {"class":"luna-pos"})
    print(input_word+" : "+ pos[0].text.replace(",", ""))
    meanings = soup.findAll("span", {"class":"one-click-content css-1p89gle e1q3nk1v4"})
except:
    print("word not found, enter correct wor to get the mening")
    exit(-1)
# print(len(meanings))
for i in range(1,4):
    print("meaning {} - {}".format(i, meanings[i].text))


