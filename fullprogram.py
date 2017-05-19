import my_fcns,re,bs4

url1='http://www.crackact.com/update.php'
url='http://www.crackact.com/update.php'
pat=re.compile(r'http:\/\/www.crackact\.com\/act-downloads\/\d+\.html')

soup=my_fcns.makesoup(url) 
for link in soup.find_all('a',href=pat):
	#print(link)
	x=link.get('href')
	y=link.get('text')
	print(link)
	with open('alist1.txt', 'a') as wf:
		wf.write(str(link))
		wf.write('\n')


