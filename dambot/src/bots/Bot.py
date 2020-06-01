from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self, color_boolean):
        if not isinstance(color_boolean, bool):
            # throw error
            return
        self.color_boolean = color_boolean  # True if white
        self.bot_name = None

    @abstractmethod
    def choose_move(self, logic_board):
        pass
