from dambot.data import StartPositions
from dambot.src.game.GameSave import Game
import time

start = time.time()

game = Game()

piece_list = StartPositions.start_piece_list(game)
game.start_player = True
game.set_board(piece_list)

game.run()

end = time.time()
print(str(end - start) + " seconds")