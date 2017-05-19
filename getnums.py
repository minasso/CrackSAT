with open('linxx.txt', 'r') as rf:
	f_contents = rf.read()

new_contents=f_contents.replace('http://www.cracksat.net/sat-downloads/', "")
new_contents=new_contents.replace('.html', "")
#key="http://www.cracksat.net/plus/download.php?open=0&aid="+key+"&cid=3"

array= new_contents.split()
#print(array)

ordered=sorted(array)

print(len(ordered))
'''
for key in ordered:
'''