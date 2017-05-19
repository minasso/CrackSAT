with open('plus.txt', 'r') as rf:
	f_contents = rf.read()
	new_contents=f_contents.replace('/plus', "www.cracksat.net/plus") 
	with open('plus2.txt', 'w') as wf:
		wf.write(new_contents)

	with open('metadata.pdf', 'wb') as f:
    f.write(response.content)