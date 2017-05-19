with open('linx.txt', 'r+') as file_contents:
	#new_contents=file_contents.read().replace('a><a', "a>\n\n<a")
	new_contents=file_contents.read().replace('\n\n', "\n")
	file_contents.seek(0) 
	file_contents.write(new_contents)
	#print(new_contents)

