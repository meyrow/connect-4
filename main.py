import logging

import coloredlogs

from Coach import Coach
from connect4.Connect4Game import Connect4Game
from connect4.pytorch.NNet import NNetWrapper as nn
from utils import dotdict


logging.basicConfig(filename='C:/ilan/python/connect4.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
log = logging.getLogger(__name__)
coloredlogs.install(level='INFO')  # Change this to DEBUG to see more info.

args = dotdict({
    'numIters': 100,
    'numEps': 50,              # 50 Number of complete self-play games to simulate during a new iteration.
    'tempThreshold': 10,        # 15
    'updateThreshold': 0.6,     # During arena playoff, new neural net will be accepted if threshold or more of games are won.
    'maxlenOfQueue': 20000,    # 20000 Number of game examples to train the neural networks.
    'numMCTSSims': 15,          # 15 Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # 40 Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/connect-4','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})


def main():
    log.info('Loading %s...', Connect4Game.__name__)
    g = Connect4Game()

    log.info('Loading %s...', nn.__name__)
    nnet = nn(g)

    log.info('Loading the Coach...')
    c = Coach(g, nnet, args)

    if args.load_model:
        log.info("Loading 'trainExamples' from file...")
        c.loadTrainExamples()

    log.info('Starting the learning process ')
    c.learn()


if __name__ == "__main__":
    main()
