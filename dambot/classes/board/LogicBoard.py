class LogicBoard:
    def __init__(self, state):
        self.state = state
        self.possible_moves = []
        self._draw_move_counter = -1
        self.number_of_pieces = len([a for a in self.state if a not in [0, "0", None]])
        self._white_has_king = False
        self._black_has_king = False
        self._past_state_hash_list = []

    def play_move(self, from_field, to_field):
        if self.state[from_field] in [0, "0", None] or self.state[to_field] not in [0, "0", None]:
            # Error
            return

        self.state[to_field] = self.state[from_field]
        self.state[from_field] = 0

        if self._draw_move_counter > -1:
            self._draw_move_counter = self._draw_move_counter - 1

        if self.state[to_field] not in [0, "0", None] and str(self.state[to_field])[1] == "s":
            self._past_state_hash_list = []

        if self._white_has_king and self._black_has_king:
            self._past_state_hash_list.append(hash(tuple(self.state)))

    def update_possible_moves(self, player_turn):
        number_of_pieces_to_take = 0
        move_list = []
        for field_enumeration in range(len(self.state)):
            field = self.state[field_enumeration]
            # If no piece is found in this field, continue
            if field == "0" or field == 0 or field is None:
                continue

            # If piece is not of color whose turn it is, continue
            if (player_turn and (field == "bs" or field == "bk")) or (not player_turn and (field == "ws" or field == "wk")):
                continue

            # If soldier is of color whose turn it is
            if (player_turn and field == "ws") or (not player_turn and field == "bs"):
                take_move_list = [[field_enumeration, field_enumeration], []]
                take_move_list = self.get_take_move_list(take_move_list, player_turn)
                # If this piece can take less pieces than a piece checked before
                if len(take_move_list) > 0 and number_of_pieces_to_take > 0 and len(take_move_list[0][1]) < number_of_pieces_to_take:
                    continue

                # If piece can take
                if len(take_move_list[0][1]) > 0:
                    # If piece can take most pieces, empty move_list
                    if len(take_move_list[0][1]) > number_of_pieces_to_take:
                        move_list = []
                        number_of_pieces_to_take = len(take_move_list[0][1])

                    # append moves to move_list
                    for take_move in take_move_list:
                        move_list.append(take_move)

                    continue

                # Else return empty fields soldier can move to
                if player_turn and field == "ws":
                    possible_fields = [field_enumeration - 10, field_enumeration - 1]

                    for possible_field_enumeration in possible_fields:
                        if (self.state[possible_field_enumeration] == "0" or self.state[possible_field_enumeration] == 0) \
                                and possible_field_enumeration > 0:
                            move_list.append([[field_enumeration, possible_field_enumeration], []])
                else:
                    possible_fields = [field_enumeration + 10, field_enumeration + 1]

                    for possible_field_enumeration in possible_fields:
                        if possible_field_enumeration < 100 and \
                                (self.state[possible_field_enumeration] == "0" or self.state[possible_field_enumeration] == 0):
                            move_list.append([[field_enumeration, possible_field_enumeration], []])

            # If king is of color whose turn it is
            if (player_turn and field == "wk") or (not player_turn and field == "bk"):
                take_move_list = [[field_enumeration, field_enumeration], []]
                take_move_list = self.get_take_move_list(take_move_list, player_turn)
                # If this piece can take less pieces than a piece checked before
                if len(take_move_list) > 0 and number_of_pieces_to_take > 0 and len(take_move_list[0][1]) < number_of_pieces_to_take:
                    continue

                # If piece can take
                if len(take_move_list[0][1]) > 0:
                    # If piece can take most pieces, empty move_list
                    if len(take_move_list[0][1]) > number_of_pieces_to_take:
                        move_list = []
                        number_of_pieces_to_take = len(take_move_list[0][1])

                    # append moves to move_list
                    for take_move in take_move_list:
                        move_list.append(take_move)

                    continue

                direction_list = [-10, -1, 1, 10]

                for direction in direction_list:
                    i = 1
                    possible_field_enumeration = field_enumeration + i * direction
                    while 0 < possible_field_enumeration < 100 and (self.state[possible_field_enumeration] == "0" or self.state[possible_field_enumeration] == 0):
                        move_list.append([[field_enumeration, possible_field_enumeration], []])
                        i = i + 1
                        possible_field_enumeration = field_enumeration + i * direction

        self.possible_moves = move_list
        return

    # recursive function
    # for every possible field where it can land, call itself
    # keep track of max length of taken_pieces_array, only return options equalling this length
    # return array of arrays (array of start- and end field and pieces that have been taken)
    def get_take_move_list(self, move, player_turn):
        return_move_list = [move]
        start_field_enumeration = move[0][0]
        field_enumeration = move[0][1]
        taken_pieces_array = move[1]
        direction_list = [-10, -1, 10, 1]
        piece_last_letter = self.state[start_field_enumeration][1]

        if player_turn:
            takeable_piece_start_letter = "b"
        else:
            takeable_piece_start_letter = "w"

        # for each neighboring field
        for direction in direction_list:
            i = 1
            possible_field_enumeration = field_enumeration + direction
            # iterate until a piece is found or field is out of range
            while piece_last_letter == "k" and 0 < possible_field_enumeration < 100 and (self.state[possible_field_enumeration] == "0" or self.state[possible_field_enumeration] == 0):
                i = i + 1
                possible_field_enumeration = field_enumeration + i * direction
            # if field is filled with a piece of the other color
            if 0 < possible_field_enumeration < 100 and isinstance(self.state[possible_field_enumeration], str) and self.state[possible_field_enumeration][0] == takeable_piece_start_letter \
                    and possible_field_enumeration not in taken_pieces_array:
                j = 1
                landing_field_enumeration = possible_field_enumeration + direction
                # iterate until a piece is found or field is out of range
                while 0 < landing_field_enumeration < 100 and \
                        (self.state[landing_field_enumeration] == "0" or self.state[landing_field_enumeration] == 0 or landing_field_enumeration == start_field_enumeration):
                    temp_taken_pieces_array = taken_pieces_array + [possible_field_enumeration]
                    temp_move = [[start_field_enumeration, landing_field_enumeration], temp_taken_pieces_array]
                    continue_taking_move_list = self.get_take_move_list(temp_move, player_turn)
                    if len(continue_taking_move_list[0][1]) < len(return_move_list[0][1]):
                        # Breaks the while loop, such that it continues with the next element of the for loop.
                        # Only works because the for loop is empty after the while loop
                        break
                    elif len(continue_taking_move_list[0][1]) == len(return_move_list[0][1]):
                        return_move_list = return_move_list + continue_taking_move_list
                    else:
                        return_move_list = continue_taking_move_list

                    # break while loop for soldiers
                    if piece_last_letter != "k":
                        break
                    j = j + 1
                    landing_field_enumeration = possible_field_enumeration + j * direction

        return return_move_list

    def remove_pieces(self, pieces_list):
        for piece_enumeration in pieces_list:
            self.state[piece_enumeration] = 0
            self.number_of_pieces = self.number_of_pieces - 1

        if len(pieces_list) > 0:
            self.check_start_draw_move_counter()
            self._past_state_hash_list = []

    def promote_piece(self, piece_enumeration, player_turn):
        if piece_enumeration in [5, 14, 23, 32, 41] and self.state[piece_enumeration] == "ws":
            self.state[piece_enumeration] = "wk"
        elif piece_enumeration in [59, 68, 77, 86, 95] and self.state[piece_enumeration] == "bs":
            self.state[piece_enumeration] = "bk"
        else:
            return

        if player_turn:
            self._white_has_king = True
        else:
            self._black_has_king = True

        if self._white_has_king and self._black_has_king:
            self._past_state_hash_list.append(hash(tuple(self.state)))

        self.check_start_draw_move_counter()

    def is_game_draw(self):
        if self._draw_move_counter == 0:
            return True

        # Check 3 times same state by keeping a hashed state list
        if self._white_has_king and self._black_has_king and self._past_state_hash_list.count(hash(tuple(self.state))) > 2:
            return True

        return False

    # Check 6 and 16 move rule
    def check_start_draw_move_counter(self):
        if self._white_has_king and self._black_has_king and self.number_of_pieces > 4 and len([a for a in self.state if a not in [0, "0", None] and str(a)[1] == "s"]) > 0:
            return

        white_kings_counter = 0
        black_kings_counter = 0
        for field_enumeration in range(99):
            if self.state[field_enumeration] is None or self.state[field_enumeration] == 0 or self.state[field_enumeration] == "0":
                continue

            if str(self.state[field_enumeration])[0] == "w":
                white_kings_counter = white_kings_counter + 1
            elif str(self.state[field_enumeration])[0] == "b":
                black_kings_counter = black_kings_counter + 1
            else:
                print("error in check_start_draw_move_counter")

            if white_kings_counter > 3 or black_kings_counter > 3:
                return

        if white_kings_counter == 3 and black_kings_counter == 1 or black_kings_counter == 3 and white_kings_counter == 1:
            self._draw_move_counter = 32
        elif white_kings_counter == 2 and black_kings_counter == 1 or black_kings_counter == 2 and white_kings_counter == 1:
            self._draw_move_counter = 12
        elif white_kings_counter == 1 and black_kings_counter == 1:
            self._draw_move_counter = 1
