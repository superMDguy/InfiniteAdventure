class item:
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

	def __str__(self):
		return "A {0} is here.  \"{1}\".".format(self.name, self.desc)
class room:
	def __init__(self, name, desc, items, generator=None, relations = {}):
		self.name = name
		self.desc = desc
		self.items = items
		self.generator = generator
		self.relations = relations

	def __str__(self):
		out = "The {0} is a room.  \"{1}\".".format(self.name, self.desc)
		for item in self.items:
			out += "\n" + str(item) + "\n"

		for direction, otherRoom in self.relations.items():
			out += "{0} of {1} is {2}.".format(direction, self.name, otherRoom.name)
		return out

	def addRelation(self, direction, otherRoom):
		self.relations[direction] = otherRoom

	def addItem(self, item):
		self.items.append(item)

class game:
	def __init__(self, name, author, rooms):
		self.name = name
		self.author = author
		self.rooms = rooms

	def __str__(self):
		out = "\"{0}\" by {1} \n\n".format(self.name, self.author)
		for room in self.rooms:
			out += str(room) + "\n"
		return out

	def save(self):
		f = open((self.name+".inform"), 'w')
		f.write(str(self))
