from dambot.classes.pieces.Piece import *


class King(Piece):
    def __init__(self, game, piece_id, color, enumeration):
        super(King, self).__init__(game, piece_id, color, enumeration)
        self.piece_type = "king"

    def draw_piece(self, canvas, x, y, color):
        r = 20
        king_draw_x_offset = -2
        king_draw_y_offset = 3
        o1 = canvas.create_oval(x-r-king_draw_x_offset, y-r-king_draw_y_offset, x+r-king_draw_x_offset, y+r-king_draw_y_offset, fill=color, tags=self.tag)
        o2 = canvas.create_oval(x-r+king_draw_x_offset, y-r+king_draw_y_offset, x+r+king_draw_x_offset, y+r+king_draw_y_offset, fill=color, tags=self.tag)
        canvas.tag_bind(o1, "<Button-1>", self._click_piece)
        canvas.tag_bind(o2, "<Button-1>", self._click_piece)
        return canvas
