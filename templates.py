import pycorpora
from random import choice

def randomBuilding():
	directions = ['Up ahead', 'In front of you', 'A few steps away', 'Far off']
	adjectives = ['an old', 'a run-down', 'a new', 'a beautiful', 'an interesting', 'an abandoned', 'a sad-looking', 'eery', 'a strangely unnerving', 'an inviting', 'a strange', 'a mysterious']
	colors_pre = ['light ', 'dark ', 'fading ', 'ugly ', 'soft ', '', '', '']
	colors = ['red', 'orange', 'yellow', 'green', 'blue', 'brown', 'white', 'black', 'gray']
	buildings = ['house', 'warehouse', 'shed', 'bungalow', 'townhouse', 'hut', 'dwelling']
	phrases = ["You feel like you should check it out.", "You wonder what's inside.", "You consider going in.", "You feel drawn to go inside it."]
	
	return "{0}, you see {1} {2}{3} {4}.  {5}".format(choice(directions), choice(adjectives), choice(colors_pre), choice(colors), choice(buildings), choice(phrases))

print(randomBuilding())