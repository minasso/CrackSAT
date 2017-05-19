from urllib.request import Request, urlopen

s1 = "http://www.cracksat.net/sat-downloads/466.html"
s2 = "http://www.cracksat.net/plus/download.php?open=0&aid=309&cid=3"
s3= 'http://www.cracksat.net/plus/download.php?open=2&id=308&uhash=e31dfb494f22d6b3d5b49521'
s4= 'https://cdn.kutasoftware.com/Worksheets/PreAlg/Rounding%20Numbers.pdf'
s5= 'https://drive.google.com/file/d/0B-SjC2QWxqXRM2M4cTNGSWhaSlE/view'
s6= 'http://www.crackact.com/plus/download.php?open=2&id=125&uhash=e714dfbf2da965514fe396fb'
s7= 'https://drive.google.com/file/d/0B-SjC2QWxqXROWJVekdPZ1BFcGM/view?usp%3Dsharing'
s8= 'https://drive.google.com/file/d/0B-SjC2QWxqXRYWdwWnRIcWRYVjA/view?usp%3Dsharing'
s9= 'http://www.cracksat.net/plus/download.php?open=2&id=678&uhash=a61562c3aa9bb1215412361e'

with open('proj1extras.txt', 'r') as rf:
	f_contents = rf.read()


def dlpdf(site,filename):
	req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	with open(filename, 'wb') as wf:
		wf.write(webpage)

dlpdf(s9,'akkkk.pdf')

 

# this program worked to download a pdf from kuta