
import asyncio

from HEXGAME import Game
from itertools import product

from ALICE import Player as Alice
from BOB import Player as Bob


class Participant (object):

    def __init__ (self, Player):
        self.player = Player()
        self.score = 0
        if hasattr(self.player, 'name'):
            self.name = self.player.name
        else:
            self.name = Player.name

    def __str__ (self):
        return '%s won %d times' % (self.name, self.score)


def pairs (players):
    for pair in product(players, repeat=2):
        if pair[0] != pair[1]:
            yield pair

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    game = Game(loop=loop)

    participants = [
        Participant(Alice),
        Participant(Bob)
    ]

    winner = None
    looser = None

    for alice, bob in pairs(participants):
        print('-' * 60)
        print('%s vs %s' % (alice.name, bob.name))
        print('-' * 60)
        print('%s vs %s' % (alice.name, bob.name))
        looser, reason = game.play(alice.player, bob.player)
        print(str(game))
        game.reset()

        if looser == alice.player:
            looser = alice
            winner = bob
        else:
            looser = bob
            winner = alice

        winner.score += 1
        print('%s beats %s by %s' % (winner.name, looser.name, reason))
        print('-' * 60)

    print('-' * 60)
    for participant in sorted(participants, key=lambda p: p.score):
        print(str(participant))
    print('-' * 60)
