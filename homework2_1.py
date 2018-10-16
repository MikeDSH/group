#单例类的实现

class Cl(object):
	__instance=None
	def __new__(cls):
		if cls.__instance==None:
			cls.__instance==object.__new__(cls)
			return  cls.__instance
		else:
			return cls.__instance

#hhhhhhhhhhhhhhh
g=1
a=Cl()
b=Cl()
print(id(a))
print(id(b))