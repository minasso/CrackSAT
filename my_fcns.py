
def dl(url, filename): 

	import requests
	res = requests.get(url)
	res.raise_for_status()
	playFile = open(filename, 'wb')
	for chunk in res.iter_content(100000):
	        playFile.write(chunk)
	playFile.close()
	return

def makesoup(url):
	import requests, bs4, re
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "lxml")
	return(soup)
	
def dlpdf(site,filename):
	req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	with open(filename, 'wb') as wf:
		wf.write(webpage)

def capture2dict(readfile, writefile, pat):
	with open(readfile, 'r')  as rf:
		with open(writefile, 'w') as wf:
			for line in rf:
				f=pat.search(line)
				if f:
					a=f.group(1)
					b=f.group(2)
					print(a,b)
					d={a+': '+b+','}  #dict formatting
					print(type(d))

def capture2(readfile, writefile, pattern):
	with open(readfile, 'r')  as rf:
		with open(writefile, 'w') as wf:
			for line in rf:
				f=pattern.search(line)
				if f:
					filename = f.group(1)
					url = f.group(2)
					print(filename, url)
					# return(filename, url)

def ziplines(readfile1, separator, readfile2, writefile):
	with open(readfile1, 'r') as rf:
		hash_contents = rf.read()
	h=hash_contents.split('\n')

	with open(readfile2, 'r') as rf:
		trim_contents = rf.read()
	t=trim_contents.split('\n')


	j=[x + separator + y for x, y in zip(h, t)]
	ameld='\n'.join(j)

	print(ameld)
	 
	with open(writefile, 'w') as wf:
			wf.write(ameld)
			

def sort_file(input_file, output_file):
	with open(input_file, 'r') as rf:
		f_contents = rf.read()
		array=f_contents.split('\n')
		array.sort()
		new='\n'.join(array)
		print(new)
		with open(output_file, 'w') as wf:
			wf.write(new)
			


def stringreplace(readfile,writefile,str,repl):
	with open(readfile, "r") as rf:
	    with open(writefile, "w") as wf:
	        for line in rf:
	            wf.write(line.replace(str, repl))

def killemptylines(readfile):
	with open('1.txt', 'r+') as rf:
		for line in rf:
			if line != '\n':
				rf.write(line)