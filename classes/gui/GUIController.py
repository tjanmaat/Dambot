import math
from classes.gui.GUIView import GUIView


class GUIController:
    def __init__(self, game, master):
        self.my_gui = GUIView(master)
        self._set_board_events()
        self.game = game

    def _set_board_events(self):
        # loop over x-and y axis, drawing rectangles at the right position with alternating colors.
        for x in range(0, 10):
            for y in range(0, 10):
                string_tag = str(x) + "_" + str(y)
                if (x + y) % 2 != 0:
                    self.my_gui.canvas.tag_bind(string_tag, "<Button-1>", self._click_on_board)

    def _draw_piece_from_canvas_position(self, x, y, color):
        self._create_circle_from_canvas_position(x, y, 20, fill=color)

    def _create_circle_from_canvas_position(self, x, y, r, **kwargs):
        return self.my_gui.canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

    @staticmethod
    def _notation_to_canvas_position(field_number):
        workable_field_number = field_number - 1
        ten_fold = math.floor(workable_field_number / 10)
        rest = workable_field_number % 10
        if rest % 10 < 5:
            return 100 * rest + 75, 100 * ten_fold + 25
        else:
            return 100 * (rest - 5) + 25, 100 * ten_fold + 75

    @staticmethod
    def _canvas_position_to_notation(x, y):
        row_number_times_five = math.floor((y - 1)/50) * 5
        return row_number_times_five + math.floor((x - 2)/100) + 1

    @staticmethod
    def notation_to_enumeration(x):
        x_mod = (x - 1) % 10
        array = [41, 32, 23, 14, 5, 51, 42, 33, 24, 15]
        x_tenfolds = int((x-1)/10)
        return array[x_mod] + x_tenfolds * 11

    @staticmethod
    def enumeration_to_notation(x):
        array = [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 4, 10, 15, 0, 0, 0, 0, 0, 0, 3, 9, 14, 20, 25, 0, 0, 0,
                 0, 2, 8, 13, 19, 24, 30, 35, 0, 0, 1, 7, 12, 18, 23, 29, 34, 40, 45, 0, 6, 11, 17, 22, 28, 33, 39, 44, 50, 0,
                 0, 16, 21, 27, 32, 38, 43, 49, 0, 0, 0, 0, 26, 31, 37, 42, 48, 0, 0, 0, 0, 0, 0, 36, 41, 47, 0, 0, 0, 0,
                 0, 0, 0, 0, 46, 0, 0, 0, 0, 0]
        return array[x]

    @staticmethod
    def _canvas_position_to_enumeration(x, y):
        return GUIController.notation_to_enumeration(GUIController._canvas_position_to_notation(x, y))

    @staticmethod
    def _enumeration_to_canvas_position(x):
        return GUIController._notation_to_canvas_position(GUIController.enumeration_to_notation(x))

    # Takes an array of piece objects and draws them
    def draw_pieces_from_enumeration(self, pieces_array):
        for piece in pieces_array:
            x, y = self._enumeration_to_canvas_position(piece.enumeration)
            piece.draw_piece(self.my_gui.canvas, x, y, self.my_gui.get_piece_color(piece.color))

    def redraw_pieces_from_enumeration(self, pieces_array, player_turn):
        self.clean_all_pieces_from_board()
        self.draw_pieces_from_enumeration(pieces_array)
        self.my_gui.update_bottom_text(player_turn)

    def clean_all_pieces_from_board(self):
        for i in range(40):
            self.my_gui.canvas.delete("tag_" + str(i))

    def _click_on_board(self, event):
        notation_position = self._canvas_position_to_enumeration(event.x, event.y)
        self.game.click_on_board(notation_position)

    def display_game_won(self, player_turn):
        self.my_gui.display_win_bottom_text(player_turn)

    def display_game_draw(self):
        self.my_gui.display_draw_bottom_text()
