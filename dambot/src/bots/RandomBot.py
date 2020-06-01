from dambot.src.bots.Bot import *
import random


class RandomBot(Bot):
    def __init__(self, color_boolean):
        super().__init__(color_boolean)
        self.bot_name = "random bot"

    def choose_move(self, logic_board):
        return logic_board.possible_moves[random.randint(0, len(logic_board.possible_moves) - 1)]
