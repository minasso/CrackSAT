
with open('read.txt', 'r') as f:
	chunk_size = 100
	f_contents = f.read(chunk_size)
	while len(f_contents) > 0:

		with open('write.txt', 'a') as p:
			p.write(f_contents)
		f_contents = f.read(chunk_size)

