import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

with open('no.txt',"w") as f:
	for url in soup.find_all('a'):
		print(url.get('href'))
		f.write(url.get('href')
	
