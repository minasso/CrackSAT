import re
pattern = "http://www.cracksat.net/sat-downloads/\d{3}.html"

with open('linx.txt', 'r') as rf:
	f_contents = rf.read()


string = f_contents




array= re.findall(str(pattern), str(string),re.I|re.M)

new_contents=str(array).replace(',', "\n")

new_contents=new_contents.replace('\'', "")
new_contents=new_contents.replace('[', "")
new_contents=new_contents.replace(']', "")

for line in array:
	with open('linxx.txt', 'w') as wf:
			wf.write(new_contents)





