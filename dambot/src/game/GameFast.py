from dambot.src.game.GameAbstract import Game
from dambot.src.bots.DraftBot import DraftBot
from dambot.src.bots.RandomBot import RandomBot
from dambot.src.board.BoardController import BoardController


class GameFast(Game):
    def __init__(self):
        super().__init__()
        self.board = BoardController(self, "fast")
        self.start_player = None  # True if white starts
        self.white = RandomBot(True)
        self.black = DraftBot(False)
        self.tk = None
        self.gui = None

    # Start game without checks
    def run(self):
        self.next_move()
        return

    # Set up board
    def set_board(self, piece_list):
        self.board.set_board(piece_list, self.start_player)

    # execute a move
    def execute_move(self, enumeration_position):
        self.board.process_move(enumeration_position)

        # Check win
        if self.board.is_player_defeated():
            player_turn = self.board.logic_board.player_turn
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

        self.board.piece_selected = move[0][0]
        self.execute_move(move[0][1])
