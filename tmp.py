import re

pat=re.compile('(\d{3}): (.+) ?,')

# def capture3dict(readfile, writefile):
# 	with open(readfile, 'r')  as rf:
# 		with open(writefile, 'w') as wf:
# 			for line in rf:
# 				f=pat.search(line)
# 				if f:
# 					a=f.group(1)
# 					b=f.group(2)
# 					print(a,b)
# 					d={a+': '+b+','}  #dict formatting
# 					print(type(d))
# 					wf.write(a+': '+b+',')


# capture3dict("a2out.txt","a3out.txt")




# with open("a2out.txt", 'r+') as f:
# 	for y in f:
# 		y=y.replace(' ,','')
# 		# y=y.replace('\n','')
# 		y=y.replace(',','')
# 		f.write(y)




		# x= y.split(':')
		# print(x)
		# (key, val) = y.split(':')
		# d[key] = val





l1=[]
l2=[]
d={}
def capture2dict(readfile, writefile):
	with open(readfile, 'r')  as rf:
		with open(writefile, 'w') as wf:
			for line in rf:
				f=pat.search(line)
				if f:
					a=[f.group(1)]
					b=[f.group(2)]
					l1.append(a)
					l2.append(b)
					keys = f.group(1)
					values = f.group(2)
					d = dict(zip(l1, l2))
			print(type(d))
			print(d)

capture2dict('a2out.txt', 'a3out.txt')






keys = ['a','b']
values = ['c','d']
dictionary = dict(zip(keys, values))
print (type(dictionary))
print(dictionary)

