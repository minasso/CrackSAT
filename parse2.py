import urllib2
from bs4 import BeautifulSoup


content = urllib2.urlopen("http://link").read()
soup = BeautifulSoup(content)

with open('parseddata.txt', 'wb') as f:
    for a in soup.find_all('a', attrs={'class': 'book-title-link'}, href=True):
        print a['href']
        f.write(a['href'] + '\n')
