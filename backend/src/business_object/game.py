class Game:
    def __init__(
        self,
        player1,
        player2,
        game_mode,
        winner,
        description=None,
        timestamp=None,
        id_game=None
        ):
        self.player1 = player1
        self.player2 = player2
        self.game_mode = game_mode
        """coin or dice"""
        self.winner = winner
        """Player or None if it is a draw"""
        self.description = description
        self.timestamp = timestamp
        self.id_game = id_game


        """
    Class representing a Game.
    Attributes:
    - id_game : int
    - player1 : Player
    - player2 : Player
    - game_mode : str
    - winner : Player
    - description: str
    - timestamp : datetime
    """

    def __str__(self):
        """coinflip between Jacky and Jackie. Winner: Jackie
        """
        return f"{self.game_mode} between {self.player1.username} and {self.player2.username}. Winner: {self.winner.username}"