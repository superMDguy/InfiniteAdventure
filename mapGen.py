from base import game, room, item
from random import choice, shuffle

class genre:
    '''Template class for genre configs'''
    def __init__(self):
        self.illegal_conns = []
        self.generators = []

    def add_bad_conn(self, type1, type2, disallowed_dirs=[]):
        self.ilegal_conns.append([type1, type2, disallowed_dirs])

    def config_gens(self, *gens):
        self.generators += gens

    def isLegal(self, type1, type2, direction):
        for conn in self.illegal_conns:
            if type1 in conn and type2 in conn and direction in conn[2]:
                return False
            return True

    def generate(self, layers, layer=0, root=None, rooms=[]):
        shuffle(self.generators)
        if root is None:
            root = self.generators[0]
        rooms = []
        if layer < layers:
            rooms.append(eval("self." + root + "()"))
            for direction in ['up','down','north','east','south','west']:
                for gen in self.generators:
                    if self.isLegal(root, gen, direction):
                        try:
                            rooms += self.generate(layers, layer=layer+1, root=gen, rooms=rooms)
                        except TypeError:
                            import pdb; pdb.set_trace()
        else:
            return rooms

class cave(genre):
    '''Test genre'''
    def chamber(self):
        desc = "You are in a dim room.  You see a huge vaulted ceiling above you.  It's beautiful."
        name = "Random cave chamber"
        return room(name, desc, [], generator = "chamber")

    def tunnel(self):
        desc = "You are in a dim tunnel.  Stalactites protrude from the walls.  The ground has gravel on it."
        name = "Random tunnel"
        return room(name, desc, [], generator = "tunnel")

    def outside(self):
        desc = "You're outside.  The sun shines brightly.  Below you is the entrance to a cave."
        name = "The outside world"
        return room(name, desc, [], generator = "outside")

    def __init__(self):
        self.generators=["chamber", "chamber", "chamber", "tunnel", "tunnel", "tunnel", "tunnel", "tunnel", "outside"]
        self.illegal_conns = [["chamber", "outside", []] ,
                            ["tunnel", "outside", ['north', 'south', 'east', 'west']]] #Only allow up and down from the tunnel to outside

test_game = game("Test cave game", "superMDguy", cave().generate(3))
print(test_game)
