from tkinter import *


class GUIView:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Dambot")

        self.blackPieceColor = None
        self.whitePieceColor = None
        self.blackFieldColor = None
        self.whiteFieldColor = None
        self._set_color_schema("gray30", "LightYellow1", 'LightGoldenRod4', 'white')
        self.player_turn = None

        self.label = Label(master, text="Dambord")
        self.label.pack()

        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.textCanvas = Canvas(master, width=400, height=50)
        self.textCanvas.create_rectangle(0, 0, 500, 500, fill='white')
        self.textCanvas.pack()
        self.bottomText = self.textCanvas.create_text(200, 20, font="Times 14 bold", text="White player's turn")

        self._create_board()

    def _set_color_schema(self, black_piece_color, white_piece_color, black_field_color, white_field_color):
        self.blackPieceColor = black_piece_color
        self.whitePieceColor = white_piece_color
        self.blackFieldColor = black_field_color
        self.whiteFieldColor = white_field_color

    def get_piece_color(self, color):
        if color == "black":
            return self.blackPieceColor
        else:
            return self.whitePieceColor

    def _create_board(self):
        # loop over x-and y axis, drawing rectangles at the right position with alternating colors.
        for x in range(0, 10):
            for y in range(0, 10):
                if (x + y) % 2 == 0:
                    color = self.whiteFieldColor
                else:
                    color = self.blackFieldColor
                string_tag = str(x) + "_" + str(y)
                rectangle = self.canvas.create_rectangle(0, 0, 50, 50, fill=color, tags=string_tag)
                self.canvas.move(rectangle, 50*x, 50*y)

    def set_player_turn(self, player_turn):
        self.player_turn = player_turn

    def update_bottom_text(self, player_turn):
        if player_turn:
            self.textCanvas.itemconfigure(self.bottomText, text="White player's turn")
        else:
            self.textCanvas.itemconfigure(self.bottomText, text="Black player's turn")

    def display_win_bottom_text(self, player_turn):
        if player_turn:
            self.textCanvas.itemconfigure(self.bottomText, text="Black player won")
        else:
            self.textCanvas.itemconfigure(self.bottomText, text="White player won")

    def display_draw_bottom_text(self):
        self.textCanvas.itemconfigure(self.bottomText, text="Game was a draw")
