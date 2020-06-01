from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self):
        self.start_player = None  # True if white starts
        self.white = None
        self.black = None
        self.tk = None
        self.gui = None

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def set_board(self, piece_list):
        pass

    @abstractmethod
    def execute_move(self, enumeration_position):
        pass

    @abstractmethod
    def next_move(self):
        pass
