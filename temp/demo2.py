class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __eq__(self, other):
		return self.name == other.name and self.age == other.age
	def __hash__(self):
		return hash( (self.name, self.age) )
	def __repr__(self):
		return self.name

def whoIsOlder(players):
    # print(players)
    return max(players, key = lambda x: x.age)

A = [Person('kevin', '18'), Person('Amy','99'), Person('gg','12')]
B = [Person('kevin', '18'), Person('gg','12')]

# players = (A, B)

print(whoIsOlder(A))

#print(set(A).intersection(B))
