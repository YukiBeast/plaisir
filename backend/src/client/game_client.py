from requests import request
from src.business_object.game import Game
import os

class GameClient:
    def get_games(self) -> list[Game]:
        url = "http://0.0.0.0:5000/player"
        r = request("GET", url)
        r.raise_for_status()
        
        if r.status_code != 200:
            raise HTTPError
            
    json = r.json()
        
    json_data = r.json()
    game_list = []

    for element in json_data:
        # Extract info using dictionary keys
        player_id = element.get("player")
        username = element.get("username")
    
    # Create the Game object and add it to the list
        game_instance = Game(player=player_id, username=username)
        game_list.append(game_instance)

    return game_list