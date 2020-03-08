from dambot.classes.pieces.Piece import *


class Soldier(Piece):
    def __init__(self, game, piece_id, color, enumeration):
        super(Soldier, self).__init__(game, piece_id, color, enumeration)
        self.piece_type = "soldier"

    def draw_piece(self, canvas, x, y, color):
        r = 20
        o = canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, tags=self.tag)
        canvas.tag_bind(o, "<Button-1>", self._click_piece)
        return canvas

