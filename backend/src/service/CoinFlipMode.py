import random
from src.business.object.game_mode import GameMode
from src.business_object.game import Game

class ConFlipMode(GameMode):
    def play(self, p1, p2, choice) -> Game:
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2
    return Game(p1, p2, "coin", winner)