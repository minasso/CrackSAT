import re
pat=re.compile('(\d{3}) ?> ?.+--- ?> ?(.+)')
def capture2dict(readfile, writefile):
	
	with open(readfile, 'r')  as rf:
		with open(writefile, 'w') as wf:
			for line in rf:
				f=pat.search(line)
				if f:
					a=f.group(1)
					b=f.group(2)
					print(a,b)
					wf.write(a+': '+b+',')  #dict formatting
					wf.write('\n')

capture2dict('comb.txt', 'aoutcomb.txt')









# with open('alist3.txt', 'r') as rf:
# 	a = rf.read()
# array=a.split('\n')
# print(array)
