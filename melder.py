with open('alist4.txt', 'r') as rf:
	f_contents = rf.read()
array = f_contents.split('\n')

with open('alist6.txt', 'r') as rf:
	f2_contents = rf.read()
array2 = f2_contents.split('\n')

zipped= zip(array,array2)
x=list(zipped)
# y=''.join(x)



y="\n".join(map(str, x))

z=y.replace('http://www.crackact.com/plus/download.php?open=2&',"")

with open('alist7.txt', 'w') as wf:
		wf.write(z)

