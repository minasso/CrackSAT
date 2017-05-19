import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl= "https://twitter.com/realDonaldTrump"
thepage= urllib.request.urlopen(theurl)
soup= BeautifulSoup(thepage,"html.parser")


with open('test2.txt',"w") as f:
    f.write(soup)

