from abc import ABC, abstractmethod

class GameMode(ABC):
    @abstractmethod
    def play(self, p1, p2, *args, **kwargs) -> Game:
        """
        Executes the game logic between two players.
        Must be implemented by all child classes.
        """
        pass