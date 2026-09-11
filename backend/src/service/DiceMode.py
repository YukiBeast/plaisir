import random
from src.business_object.game_mode import GameMode

class DiceMode(GameMode):
    def play(self, p1, p2) -> Game:
        p1_roll = random.randint(1, 6)
        p2_roll = random.randint(1, 6)
        
        if p1_roll > p2_roll:
            winner = p1
        elif p2_roll > p1_roll:
            winner = p2
        else:
            winner = "Draw"
    
    return Game(p1, p2, "dice", winner)