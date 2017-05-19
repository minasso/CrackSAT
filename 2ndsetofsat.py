
import re, my_fcns
from urllib.request import Request, urlopen
pattern=re.compile('\d{3}: (.+) - (http:.+)')
readfile= '2.txt'
with open(readfile, 'r')  as rf:
	f_contents = rf.read()
array= f_contents.split('\n')
for line in array:
	f=pattern.search(line)
	if f:
		filename = f.group(1)
		site = f.group(2)
		print(filename, site)
	else:
		print('match not found')
	try:
		req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
		webpage = urlopen(req).read() 
		destination = 'C:\\Users\\andrew\\Desktop\\crackact\\%s.pdf' %(filename)
		with open(destination, 'wb') as wf:
			wf.write(webpage)
	except:
		print('error')





