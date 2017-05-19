import urllib.request
import urllib.parse

s1= "https://www.google.com/search?q=test"
s2= "http://pythonprogramming.net"
s3= 'www.cracksat.net/plus/download.php?open=2&id=308&uhash=e31dfb494f22d6b3d5b49521'
s4= 'https://cdn.kutasoftware.com/Worksheets/PreAlg/Rounding%20Numbers.pdf'
url= s4


try:
	url = s1

	headers= {}
	headers['User-Agent']= 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	req= urllib.request.Request(url, headers=headers)
	resp= urllib.request.urlopen(req)
	respData= resp.read()

	saveFile= open('onek.txt', 'w')
	saveFile.write(str(respData))
	saveFile.close()

except Exception as e:
	print(str(e))

