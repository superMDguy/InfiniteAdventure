import base, mapGen

flower = item("flower", "A beautiful pink rose")
livingRoom = room("living room", "You can see some old furniture in this aging room", [flower])
bedroom = room("bedroom", "You can see a bed and some clothes on the ground", [])
livingRoom.addRelation("up", anotherRoom)
game = game("Test", "Matthew D.", [livingRoom, bedroom])
print(game)
game.save()
