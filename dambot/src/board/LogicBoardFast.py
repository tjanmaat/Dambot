import copy

from dambot.src.board.LogicBoardAbstract import LogicBoard


class LogicBoardFast(LogicBoard):
    def __init__(self, state=None, player_turn=None):
        super().__init__(state, player_turn)

    # Changes state of board
    # Using process_move instead is recommended
    def _play_move(self, from_field, to_field):
        self.state[to_field] = self.state[from_field]
        self.state[from_field] = 0

        if self._draw_move_counter > -1:
            self._draw_move_counter = self._draw_move_counter - 1

        if self.state[to_field] not in [0, "0", None] and str(self.state[to_field])[1] == "s":
            self._past_state_hash_list = []

        if self._white_has_king and self._black_has_king:
            self._past_state_hash_list.append(hash(tuple(self.state)))
