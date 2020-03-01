import StartPositions
from classes.game.Game import Game
import time

start = time.time()

for i in range(500):

    game = Game()

    piece_list = StartPositions.start_piece_list(game)
    game.player_turn = True
    game.set_board(piece_list)

    game.run()

end = time.time()
print(str(end - start) + " seconds")

# TODO's
# Implement error reporting
# pop-up asking for pc/human players
