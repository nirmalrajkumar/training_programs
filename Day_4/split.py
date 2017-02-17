import os

def cl():

	f = file('/home/ids/Desktop/Documents/abc/fiile.text','r')
	a=f.read()
	b = a.split("\n")
	for c in b:
		k = c.split(' ')
		print k[0]
	return k;

for d in cl():
   print d




