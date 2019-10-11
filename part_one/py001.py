# 一摞有序的纸牌 __getitem__ 和 __len___
# import sys
# sys.path.extend(['/Users/pan/Codes-01/PY/python_test001'])


import collections
import doctest

Card = collections.namedtuple('Card', ['rank', 'suit'])
"""
>>> beer_card = Card(7,'ssss')
>>> beer_card
Card(rank=7, suit='ssss')

"""


class FrenchDeck:
    """
    定义一个纸牌类
>>> FrenchDeck.ranks
['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
>>> FrenchDeck.suit
['spades', 'diamonds', 'clubs', 'hearts']
    >>> deck = FrenchDeck()
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]

>>> deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
>>> for i in deck[:4]: # doctest: +ELLIPSIS
...     print(i)
...
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
Card(rank='5', suit='spades')
>>> for i in reversed(deck[:4]): # doctest: +ELLIPSIS
...     print(i)
...
Card(rank='5', suit='spades')
Card(rank='4', suit='spades')
Card(rank='3', suit='spades')
Card(rank='2', suit='spades')



    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.ranks]  # 全排列

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    doctest.testmod(verbose=True)
