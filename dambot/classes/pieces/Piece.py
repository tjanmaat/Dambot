from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, game, piece_id, color, enumeration):
        # check input values
        self.game = game
        self.id = piece_id
        self.color = color
        self.enumeration = enumeration
        self.piece_type = None
        self.tag = "tag_" + str(self.id)

    @abstractmethod
    def draw_piece(self, canvas, x, y, color):
        pass

    def _click_piece(self, event):
        self.game.click_on_board(self.enumeration)
