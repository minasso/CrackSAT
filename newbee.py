import bs4 as bs   #beautiful soup library to beautify/parse data
from urllib.request import Request, urlopen
import re
s1='http://www.cracksat.net/sat-downloads/new-sat.html'
s2='https://pythonprogramming.net/parsememcparseface/'
s3='https://pythonprogramming.net/sitemap.xml'
s4='http://www.cracksat.net/plus/download.php?open=0&aid=669&cid=3'
s5='http://www.cracksat.net/plus/download.php?open=2&id=516&uhash=9507e6f6cd3bef92b7f8d143'
with open('plus2.txt', 'r') as rf:
	f_contents = rf.read()
	new_contents=f_contents.replace('www', "http://www")
	array=new_contents.split('\n')
site=s5
test= array[4:9]

with open('codes.txt', 'a') as wf:
	for site in test2:
		try:
			req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
			webpage = urlopen(req).read()
			soup = bs.BeautifulSoup(webpage, 'lxml')
			lines= soup.find_all('a',href=re.compile('h'))
			linex= soup.find('a',href=re.compile('h'))
			ref= linex.get('href')
			new_contents=ref.replace('https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&continue=https://drive.google.com/file/d/', "")
			new_contents=new_contents[:28]
			
			print(new_contents)
			wf.write(new_contents)
			wf.write('\n')
		except AttributeError:
			wf.write(site)
			print('error')







