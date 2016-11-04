from base import game, room, item
from random import choice, shuffle
import logging

#logging.basicConfig(level=logging.DEBUG)

class genre:
	'''Superlass for genre configs'''
	def __init__(self):
		raise NotImplementedError("You need to implement __init__ in your genre to set up self.generator and self.illegal_conns")

	def add_bad_conn(self, type1, type2, disallowed_dirs=[]):
		self.ilegal_conns.append([type1, type2, disallowed_dirs])

	def isLegal(self, type1, type2, direction):
		for conn in self.illegal_conns:
			if type1 in conn and type2 in conn and direction in conn[2]:
				return False
			return True

	def generate(self, layers, layer=0, root=None, rooms=[]):
		shuffle(self.generators)
		if root is None:
			root = eval("self." + self.generators[0] + "()")
		if layer < layers:
			for direction in ['up','down','north','east','south','west']:
				for gen in self.generators:
					if self.isLegal(root.generator, gen, direction):
						room = eval("self." + gen + "()")
						root.addRelation(direction, room)
						rooms.append(room)
						rooms = self.generate(layers, layer=layer+1, root=room, rooms=rooms)
			return rooms
		else:
			logging.info("Reached max layer.")
			logging.debug("Rooms:")
			for room in rooms:
				logging.debug(room)
			return rooms

class cave(genre):
	'''Test genre'''
	def chamber(self):
		desc = "You are in a dim room.  You see a huge vaulted ceiling above you.  It's beautiful."
		name = "Random cave chamber" + str(self.id)
		self.id += 1
		return room(name, desc, [], "chamber")

	def tunnel(self):
		desc = "You are in a dim tunnel.  Stalactites protrude from the walls.  The ground has gravel on it."
		name = "Random tunnel" + str(self.id)
		self.id += 1
		return room(name, desc, [], "tunnel")

	def outside(self):
		desc = "You're outside.  The sun shines brightly.  Below you is the entrance to a cave."
		name = "The outside world" + str(self.id)
		self.id += 1
		return room(name, desc, [], "outside")

	def __init__(self):
		self.id = 1
		self.generators=["chamber", "chamber", "chamber", "tunnel", "tunnel", "tunnel", "tunnel", "tunnel", "outside"]
		self.illegal_conns = [["chamber", "outside", []] ,
							["tunnel", "outside", ['north', 'south', 'east', 'west']]] #Only allow up and down from the tunnel to outside

test_game = game("Test cave game", "superMDguy", cave().generate(2))
test_game.save()
