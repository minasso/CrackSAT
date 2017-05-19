import re
with open('linx.txt', 'r') as rf:
	f_contents = rf.read()
	new_contents=f_contents.replace('<a href=', "")
	with open('href.txt', 'w') as wf:
			wf.write(new_contents)