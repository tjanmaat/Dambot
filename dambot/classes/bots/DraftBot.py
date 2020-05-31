from dambot.classes.bots.Bot import *
from dambot.classes.board.LogicBoard import LogicBoard
import random


class DraftBot(Bot):
    def __init__(self, color_boolean):
        super().__init__(color_boolean)
        self.bot_name = "draft bot"

    def choose_move_2_old(self, logic_board):
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
            temp_logic_board.process_move(possible_move)

            # score: 0 is this bot wins, 1 is this bot loses.
            score = 0

            # check all opponent possible moves.
            # State with best score for opponent is taken as realistic.
            for possible_opponent_move in temp_logic_board.possible_moves:
                nested_temp_logic_board = LogicBoard(temp_logic_board.state)
                nested_temp_logic_board._play_move(possible_opponent_move[0][0], possible_opponent_move[0][1])
                nested_temp_logic_board.remove_pieces(possible_opponent_move[1])
                move_score = self._evaluate_board_state(nested_temp_logic_board)
                if move_score > score:
                    score = move_score

            if score < best_move_score:
                best_move_score = score
                best_move_list = [possible_move]
            elif score == best_move_score:
                best_move_list.append(possible_move)

        return best_move_list[random.randint(0, len(best_move_list) - 1)]

    def choose_move_3_old(self, logic_board):
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
            temp_logic_board.process_move(possible_move)

            # score: 0 is this bot wins, 1 is this bot loses.
            score = 0

            # check all opponent possible moves.
            # State with best score for opponent is taken as realistic.
            for possible_opponent_move in temp_logic_board.possible_moves:
                nested_temp_logic_board = LogicBoard(temp_logic_board.state)
                nested_temp_logic_board.process_move(possible_opponent_move)

                nested_score = 1

                # check all possible moves.
                # State with best score is taken as realistic.
                for possible_own_move in nested_temp_logic_board.possible_moves:
                    nested_2_temp_logic_board = LogicBoard(nested_temp_logic_board.state)
                    nested_2_temp_logic_board._play_move(possible_own_move[0][0], possible_own_move[0][1])
                    nested_2_temp_logic_board.remove_pieces(possible_own_move[1])
                    move_score = self._evaluate_board_state(nested_2_temp_logic_board)
                    if move_score < nested_score:
                        nested_score = move_score

                if nested_score > score:
                    score = nested_score

            if score < best_move_score:
                best_move_score = score
                best_move_list = [possible_move]
            elif score == best_move_score:
                best_move_list.append(possible_move)

        return best_move_list[random.randint(0, len(best_move_list) - 1)]

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
            temp_logic_board = LogicBoard(logic_board.state, logic_board.player_turn)
            temp_logic_board.process_move(possible_move)

            # score: 0 is this bot wins, 1 is this bot loses.
            score = self._best_move_n_deep(temp_logic_board, 3, 2)

            if score < best_move_score:
                best_move_score = score
                best_move_list = [possible_move]
            elif score == best_move_score:
                best_move_list.append(possible_move)

        return best_move_list[random.randint(0, len(best_move_list) - 1)]

    # Current_depth counts down from total_depth to 1
    def _best_move_n_deep(self, logic_board, total_depth, current_depth):
        # If this is the 1st iteration and there's only one move to choose from, pick that move
        if total_depth == current_depth and len(logic_board.possible_moves) == 1:
            return logic_board.possible_moves[0]
        print("depth: " + str(current_depth))

        player_move = (total_depth % 2 == current_depth % 2)

        # score: 0 is this bot wins, 1 is this bot loses.
        if player_move:
            score = 1
        else:
            score = 0

        for possible_move in logic_board.possible_moves:
            temp_logic_board = LogicBoard(logic_board.state, logic_board.player_turn)
            temp_logic_board._play_move(possible_move[0][0], possible_move[0][1])
            temp_logic_board.remove_pieces(possible_move[1])

            if current_depth == 1:
                move_score = self._evaluate_board_state(temp_logic_board)
            else:
                temp_logic_board.promote_piece(possible_move[0][1])
                temp_logic_board.player_turn = not temp_logic_board.player_turn
                temp_logic_board.update_possible_moves()
                move_score = self._best_move_n_deep(temp_logic_board, total_depth, current_depth - 1)
                print("depth: " + str(current_depth))

            if (player_move and move_score < score) or (not player_move and move_score > score):
                print("move_score: " + str(move_score))
                score = move_score

        return score

    def _evaluate_board_state(self, logic_board):
        number_of_white_pieces = len([a for a in logic_board.state if a in ["ws", "wk"]])
        if self.color_boolean:
            return 1 - number_of_white_pieces / logic_board.number_of_pieces
        else:
            return number_of_white_pieces / logic_board.number_of_pieces
