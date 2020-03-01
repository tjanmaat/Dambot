from classes.board.LogicBoard import LogicBoard
from classes.pieces.Soldier import Soldier
from classes.pieces.King import King


class BoardController:
    def __init__(self, game):
        self.piece_selected = None
        self.logic_board = None
        self.game = game

    def set_board(self, piece_list, player_turn):
        self.logic_board = LogicBoard(BoardController._piece_list_to_state(piece_list))
        self.logic_board.update_possible_moves(player_turn)

    def get_board(self):
        return self._state_to_piece_list(self.logic_board.state)

    def play_move(self, to_field, player_turn):
        for possible_move in self.logic_board.possible_moves:
            if [self.piece_selected, to_field] == possible_move[0]:
                self.logic_board.play_move(self.piece_selected, to_field)
                self.logic_board.remove_pieces(possible_move[1])
                self.logic_board.promote_piece(possible_move[0][1], player_turn)
                self.logic_board.update_possible_moves(not player_turn)
                return True
        return False

    @staticmethod
    def _piece_list_to_state(piece_list):
        state = [None, None, None, None, None, 0, None, None, None, None, None, None, None, None, 0, 0, 0, None, None, None,
                 None, None, None, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, None,
                 None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 None, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, 0, None, None,
                 None, None, None, None, 0, 0, 0, None, None, None, None, None, None, None, None, 0, None, None, None, None]
        for piece in piece_list:
            state[piece.enumeration] = BoardController._piece_to_abbreviation(piece)
        return state

    def _state_to_piece_list(self, state):
        piece_list = []
        for field in range(len(state)):
            if state[field] == "ws":
                piece_list.append(Soldier(self.game, len(piece_list), "white", field))
            elif state[field] == "bs":
                piece_list.append(Soldier(self.game, len(piece_list), "black", field))
            elif state[field] == "wk":
                piece_list.append(King(self.game, len(piece_list), "white", field))
            elif state[field] == "bk":
                piece_list.append(King(self.game, len(piece_list), "black", field))
        return piece_list

    @staticmethod
    def _piece_to_abbreviation(piece):
        if piece.color == "white":
            if piece.piece_type == "soldier":
                return "ws"
            elif piece.piece_type == "king":
                return  "wk"
        elif piece.color == "black":
            if piece.piece_type == "soldier":
                return "bs"
            elif piece.piece_type == "king":
                return  "bk"
        # error

    def is_field_occupied(self, notation_position):
        return self.logic_board.state[notation_position] != "0" and self.logic_board.state[notation_position] != 0 \
               and self.logic_board.state[notation_position] is not None

    def check_field_has_piece_of_player_turn(self, enumeration_position, player_turn):
        if player_turn:
            if str(self.logic_board.state[enumeration_position])[0] == "w":
                return True
        else:
            if str(self.logic_board.state[enumeration_position])[0] == "b":
                return True
        return False

    def is_player_defeated(self):
        return len(self.logic_board.possible_moves) == 0

    def is_game_draw(self):
        return self.logic_board.is_game_draw()

    def check_valid_board(self):
        none_field_array = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 28, 29, 30, 31, 39, 40,
                            50, 60, 61, 69, 70, 71, 72, 78, 79, 80, 81, 82, 83, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97,
                            98, 99]
        for none_field in none_field_array:
            if self.logic_board.state[none_field] is not None:
                return False
        return True
