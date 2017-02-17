class rec:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def rect(self):
		return self.a*self.b
	def __str__(self):
		return str(self.a)+str(self.b)
	def pe(self):
		return 2* self.a+ self.b

c=rec(15,40)
c.rect()
print c
print c.rect()
print c.pe()

