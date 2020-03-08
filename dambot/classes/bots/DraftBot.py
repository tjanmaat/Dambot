from dambot.classes.bots.Bot import *
from dambot.classes.board.LogicBoard import LogicBoard
import random


class DraftBot(Bot):
    def __init__(self, color_boolean):
        super().__init__(color_boolean)
        self.bot_name = "draft bot"

    def choose_move(self, logic_board):
        if len(logic_board.possible_moves) == 1:
            return logic_board.possible_moves[0]

        # this should be done with a function that returns a score.
        # Then the line that calls _evaluate_board_state, could call that function instead.
        # That would enable looking a move further
        best_move_score = 1
        best_move_list = []
        # for each possible move, check all the opponents moves. If he can take pieces
        for possible_move in logic_board.possible_moves:
            temp_logic_board = LogicBoard(logic_board.state)
            temp_logic_board.play_move(possible_move[0][0], possible_move[0][1])
            temp_logic_board.remove_pieces(possible_move[1])
            temp_logic_board.promote_piece(possible_move[0][1], self.color_boolean)
            temp_logic_board.update_possible_moves(not self.color_boolean)

            # score: 0 is this bot wins, 1 is this bot loses.
            score = 1

            # check all opponent possible moves. State with best score for opponent is taken as realistic.
            # todo: check if best opponent move is indeed assumed
            for possible_opponent_move in temp_logic_board.possible_moves:
                nested_temp_logic_board = LogicBoard(temp_logic_board.state)
                nested_temp_logic_board.play_move(possible_opponent_move[0][0], possible_opponent_move[0][1])
                nested_temp_logic_board.remove_pieces(possible_opponent_move[1])
                move_score = self._evaluate_board_state(nested_temp_logic_board)
                if move_score < score:
                    score = move_score

            if score < best_move_score:
                best_move_score = score
                best_move_list = [possible_move]
            elif score == best_move_score:
                best_move_list.append(possible_move)

        return best_move_list[random.randint(0, len(best_move_list) - 1)]

    def _evaluate_board_state(self, logic_board):
        number_of_white_pieces = len([a for a in logic_board.state if a in ["ws", "wk"]])
        if self.color_boolean:
            return 1 - number_of_white_pieces / logic_board.number_of_pieces
        else:
            return number_of_white_pieces / logic_board.number_of_pieces
