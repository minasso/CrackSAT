import bs4 as bs
from urllib.request import Request, urlopen
import re



s5 = 'http://www.cracksat.net/plus/download.php?open = 2&id = 516&uhash = 9507e6f6cd3bef92b7f8d143'

with open('alist4.txt', 'r') as rf:
	f_contents  =  rf.read()
	array = f_contents.split('\n')

test =  array[7:9]

for site in array:
	try:
		req  =  Request(site, headers = {'User-Agent': 'Mozilla/5.0'})
		webpage  =  urlopen(req).read()
		soup  =  bs.BeautifulSoup(webpage, 'lxml')
		# lines =  soup.find_all('a',href = re.compile('h'))
		linex =  soup.find('a',href = re.compile('h'))
		ref =  linex.get('href')
		print(ref)
		new_contents = ref.replace('https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&continue=https://drive.google.com/file/d/0B-SjC2QWxqXRZWtMRVVMRWg1ZkU/view?usp%3Dsharing&followup=', "")
		with open('alist5.txt', 'a') as wf:
			print(new_contents)
			wf.write(new_contents)
			wf.write('\n')
	except AttributeError:
		print('attribute error')







