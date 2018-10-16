
from HEXGAME import AbstractPlayer, HORIZ, VERTI, EMPTY, COLS, ROWS
import random

class Player (AbstractPlayer):

    name = 'Bob'

    def play(self, board, direction, **options):

        x = random.randrange(COLS)
        y = random.randrange(ROWS)

        while board[x][y] != EMPTY:
            x = random.randrange(COLS)
            y = random.randrange(ROWS)

        return (x, y)
