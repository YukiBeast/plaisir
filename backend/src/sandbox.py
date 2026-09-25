# uv run --project backend python backend/src/sandbox.py
from business_object.game import Game
from business_object.player import Player
from dao.game_dao import GameDao
from utils.env_variables import load_environment_variables
from datetime import datetime, timezone

load_environment_variables()   # Required to load the variables needed (env) to connect to the database 

p1 = Player(username="gi", elo=100, email="a", id_player=1)
p2 = Player(username="gigi", elo=100, email="b", id_player=2)
game = Game(p1, p2, "dice", p1, description="g vs g", timestamp=datetime.now(), id_game=6)

id = GameDao().create(game)
print(id)
game2 = GameDao().find_by_id(6)
