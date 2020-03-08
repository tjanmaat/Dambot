from dambot.classes.bots.Bot import *


class Player(Bot):
    def __init__(self, color_boolean):
        super().__init__(color_boolean)
        self.bot_name = "player"

    def choose_move(self, logic_board):
        return []
