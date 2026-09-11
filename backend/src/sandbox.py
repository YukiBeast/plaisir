from business_object.game import Game
from business_object.player import Player

p1 = Player("paul", 1, "p")
p2 = Player("bob", 2, "b")
g = Game(p1, p2, "dice", p1)
print(g)