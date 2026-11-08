class Person:
	name = "anonymous"
	def changeName(self, name):
		Person.name = name

p1 = Person()        
p1.changeName("John")
print(p1.name)
print(Person.name)
