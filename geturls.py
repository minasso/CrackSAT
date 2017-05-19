import bs4 as bs
from urllib.request import Request, urlopen
import re

s1='http://www.cracksat.net/sat-downloads/new-sat.html'
s2='https://pythonprogramming.net/parsememcparseface/'
s3='https://pythonprogramming.net/sitemap.xml'
site=s2


req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = bs.BeautifulSoup(webpage, 'lxml')
print(soup)
