from datetime import datetime
from random import choice, seed

class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()


# Logger class Dictionary overview
print(Logger.__dict__)


# instance of logger
l = Logger()

print(l.current_time)


class Deck:
    @property
    def suit(self):
        return choice(('Spade', 'Heart', 'Diamond', 'Club'))

    @property
    def card(self):
        return choice(tuple('23456789JQKA') + ('10', ))


# Instance of Deck
d = Deck()
seed(0)

for _ in range(10):
    print(d.card, d.suit)


class Choice:
    def __init__(self, *choices):
        self.choices = choices

    def __get__(self, instance, owner_class):
        return choice(self.choices)


# Deck redefined
class Deck1:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')


seed(0)

d1 = Deck1()
for _ in range(10):
    print(d1.card, d1.suit)


# class Dice
class Dice:
    die_1 = Choice(1, 2, 3, 4, 5, 6)
    die_2 = Choice(1, 2, 3, 4, 5, 6)
    die_3 = Choice(1, 2, 3, 4, 5, 6)


seed(0)
dice = Dice()

for _ in range(10):
    print(dice.die_1, dice.die_2, dice.die_3)

