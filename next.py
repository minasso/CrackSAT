import bs4 as bs
from urllib.request import Request, urlopen
import json
import re

s1='http://www.cracksat.net/sat-downloads/new-sat.html'
s2='https://pythonprogramming.net/parsememcparseface/'
s3='https://pythonprogramming.net/sitemap.xml'
s4='http://www.cracksat.net/sat-downloads/683.html'
site=s4


req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

for url in soup.find_all('a', href=re.compile('plus')):
	print(url.get('href'))

# with open('linxxx.txt', 'w') as wf:
#     for line in soup.find_all('a', href=re.compile("http://www.cracksat.net/sat-downloads")):
#         wf.write(str(line))


#/plus/download.php?open=0&aid=\d{3}&cid=\d