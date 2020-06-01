from dambot.src.gui.GUIController import GUIController
from dambot.src.pieces.Soldier import Soldier
from dambot.src.pieces.King import King


def test_piece_list_one(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(11)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  King(game, 5, "white", GUIController.notation_to_enumeration(49))]
    return piece_list


def test_piece_list_two(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(7)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(8)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(18)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(19)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(29)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  King(game, 5, "white", GUIController.notation_to_enumeration(49))]
    return piece_list


def test_piece_list_three(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(1)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(7)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(8)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(18)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(19)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(29)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(14)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  King(game, 5, "white", GUIController.notation_to_enumeration(49))]
    return piece_list


def test_piece_list_four(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(1)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(7)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(8)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(17)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(18)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(19)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(29)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(33)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  King(game, 5, "white", GUIController.notation_to_enumeration(49))]
    return piece_list


def test_piece_list_five(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(1)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(7)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(8)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(17)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(18)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(19)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(29)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(13)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  King(game, 5, "white", GUIController.notation_to_enumeration(49))]
    return piece_list


def test_piece_list(game):
    piece_list = [Soldier(game, 5, "white", GUIController.notation_to_enumeration(6)),
                  Soldier(game, 5, "black", GUIController.notation_to_enumeration(45))]
    return piece_list


def start_piece_list(game):
    piece_list = [Soldier(game, 1, "black", GUIController.notation_to_enumeration(1)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(2)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(3)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(4)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(5)),
                  Soldier(game, 1, "black", GUIController.notation_to_enumeration(6)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(7)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(8)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(9)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(10)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(11)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(12)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(13)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(14)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(15)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(16)),
                  Soldier(game, 2, "black", GUIController.notation_to_enumeration(17)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(18)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(19)),
                  Soldier(game, 3, "black", GUIController.notation_to_enumeration(20)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(31)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(32)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(31)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(32)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(33)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(34)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(35)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(36)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(37)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(38)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(39)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(40)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(41)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(42)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(43)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(44)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(45)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(46)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(47)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(48)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(49)),
                  Soldier(game, 4, "white", GUIController.notation_to_enumeration(50))]
    return piece_list
