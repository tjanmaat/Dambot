from tkinter import *

from dambot.src.gui.GUIController import GUIController
from dambot.src.game.GameAbstract import Game
from dambot.src.bots.DraftBot import DraftBot
from dambot.src.bots.Player import Player
from dambot.src.bots.RandomBot import RandomBot
from dambot.src.board.BoardController import BoardController


class GameSave(Game):
    def __init__(self):
        super().__init__()
        self.board = BoardController(self, "save")
        self.start_player = None  # True if white starts
        self.white = Player(True)
        self.black = DraftBot(False)
        self.tk = None
        self.gui = None

    # Start game
    def run(self):
        if not isinstance(self.start_player, bool):
            return

        if not self.board.check_valid_board():
            return

        # check if first move is non-human
        self.next_move()

        # If there is a board, draw it
        if self.tk is not None:
            self.tk.mainloop()

    # Set up board
    def set_board(self, piece_list):
        self.board.set_board(piece_list, self.start_player)

        # If a human player exists, create board gui
        if self.white.bot_name == "player" or self.black.bot_name == "player":
            self.tk = Tk()
            self.gui = GUIController(self, self.tk)
            self.gui.draw_pieces_from_enumeration(self.board.get_board())

    # handle click on board event
    def click_on_board(self, enumeration_position):
        # If clicked field is occupied and of right color, select piece
        # If field is empty and a piece was selected already, play move
        if self.board.is_field_occupied(enumeration_position) and \
                self.board.check_field_has_piece_of_player_turn(enumeration_position):
            self.board.piece_selected = enumeration_position
            # self.gui.highlight_piece()
        elif self.board.piece_selected is not None and isinstance(self.board.piece_selected, int) and not \
                self.board.is_field_occupied(enumeration_position):
            self.execute_move(enumeration_position)


    # execute a move
    def execute_move(self, enumeration_position):
        is_move_played = self.board.process_move(enumeration_position)
        if is_move_played:
            self.board.piece_selected = None

        player_turn = self.board.logic_board.player_turn
        # If there is a board to redraw, do so
        if self.gui is not None:
            self.gui.redraw_pieces_from_enumeration(self.board.get_board(), player_turn)

        # Check win
        if self.board.is_player_defeated():
            if player_turn:
                print("Black player won")
            else:
                print("White player won")
            if self.gui is not None:
                self.gui.display_game_won(player_turn)
            return
        elif self.board.is_game_draw():
            print("Game was draw")
            if self.gui is not None:
                self.gui.display_game_draw()
            return

        # Check if next move is non-human
        self.next_move()

    # get the next move
    def next_move(self):
        move = []
        if self.board.logic_board.player_turn:
            move = self.white.choose_move(self.board.logic_board)
        elif not self.board.logic_board.player_turn:
            move = self.black.choose_move(self.board.logic_board)

        # If player is human, move is an empty array; no move is executed
        if len(move) > 0:
            self.board.piece_selected = move[0][0]
            self.execute_move(move[0][1])
