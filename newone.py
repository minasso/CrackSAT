import bs4 as bs   #beautiful soup library to beautify/parse data
from urllib.request import Request, urlopen
import re
s1='http://www.cracksat.net/sat-downloads/new-sat.html'
s2='https://pythonprogramming.net/parsememcparseface/'
s3='https://pythonprogramming.net/sitemap.xml'
s4='http://www.cracksat.net/plus/download.php?open=0&aid=669&cid=3'
site=s4


with open('linxx.txt', 'r') as rf:
	f_contents = rf.read()

new_contents=f_contents.replace('http://www.cracksat.net/sat-downloads/', "")
new_contents=new_contents.replace('.html', "")
#key="http://www.cracksat.net/plus/download.php?open=0&aid="+key+"&cid=3"

array= new_contents.split()
#print(array)
test= ['669','670','438']
ordered=sorted(array)


wf = open('plus.txt', 'a') 

for key in ordered:
	site="http://www.cracksat.net/plus/download.php?open=0&aid="+key+"&cid=3"
	req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = bs.BeautifulSoup(webpage, 'lxml')

	new=soup.find('a', href=re.compile("/plus/download"))

	try:
		ref=new.get('href')
	except AttributeError as e:
		pass
	else:
		print(ref)
		wf.write(str(ref))
		wf.write('\n')

wf.close()
'''
# for line in soup.find_all('a', href=re.compile("/plus/download")):
# 	ref= line.get('href')

#'a', href=re.compile("http://www.cracksat.net/sat-downloads/\d")
'''