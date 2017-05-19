import re
pat=re.compile('http://www.cracksat.net')


with open('newmeld.txt', 'r') as rf:
	with open('meld_trim.txt', 'w') as wf:
			
		for line in rf:
			p=pat.search(line)
			if not p:
				wf.write(line)





