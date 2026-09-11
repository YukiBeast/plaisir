import os
import secrets

from fastapi import HTTPException

from dao.player_dao import PlayerDao
from utils.log_utils import log


class GameService:
    def play(self, player_id, opponent_id, game_mode, **kwargs):

        # Find players by id -> the code does not change
        p1 = PlayerDao().find_by_id(id_player)
        p2 = PlayerDao().find_by_id(id_opponent)

        # Get rules
        mode = get_mode(game_mode)

        # Play the game following rules
        # Eventualy add extra parameters like choice (included in kwargs)
        game = mode.play(p1, p2, **kwargs)

        # Calculate Elo ratings based on the game result 
        compute(game)

        # Update Players object in the database (not this week)
        PlayerDao().update(player1)
        PlayerDao().update(player2)

        return game