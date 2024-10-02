# Modulen deck
import random
from enum import Enum

class Suit(Enum):
    Diamond = 1
    Club = 2
    Heart = 3
    Spade = 4


class Face(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

class Card:
    ftab = ('CLUB', 'DIAMOND', 'HEART', 'SPADE')
    vtab = ('A', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, _Suit, _Face):
        self._suit = _Suit
        self._face = _Face
        self._cardValue = _Face
        if _Face >10:
            self._cardValue = 10
        else:
            self._cardValue = _Face

    def get_suit(self):
        return self._suit

    def get_value_min(self):
        return self._cardValue

    def __str__(self):
        return Card.ftab[self._suit - 1] + ' ' + Card.vtab[self._face - 1]


class Deck:

    def __init__(self):
        self._deck = []
        for i in range(1, 5):
            for j in range(1, 14):
                self._deck.append(Card(i, j))
        random.shuffle(self._deck)

    def give(self):
        if len(self._deck) > 0:
            return self._deck.pop()
        else:
            return None
