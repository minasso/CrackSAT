import re
with open('alist5.txt', 'r') as rf:
	f_contents = rf.read()
pat1='https://accounts.google.com/ServiceLogin?service=wise&passive=1209600&continue='
pat2=re.compile(r'https:\/\/accounts.google.com\/ServiceLogin\?service=wise&passive=1209600&continue=https:\/\/drive.google.com\/file\/d\/0B-SjC2QWxqXR.+\/view\?usp%3Dsharing&followup=')
# pat=re.sub(pat1,"",f_contents)
pat=pat2.sub("",f_contents)
with open('alist6.txt', 'w') as wf:
		wf.write(pat)
		wf.write('\n')