import time
import multiprocessing
from dambot.data import StartPositions
from dambot.src.game.GameFast import GameFast


def basic_func(x):
    game = GameFast()

    piece_list = StartPositions.start_piece_list(game)
    game.start_player = True
    game.set_board(piece_list)

    game.run()


if __name__ == '__main__':
    starttime = time.time()
    available_processors = multiprocessing.cpu_count() - 1

    p = multiprocessing.Pool(processes=available_processors)
    p.map(basic_func, range(0, 50))
    p.close()

    print('That took {} seconds'.format(time.time() - starttime))


# TODO's
# Implement error reporting
# pop-up asking for pc/human players
