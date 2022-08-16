from enum import Enum, auto
from functools import total_ordering
from http import HTTPStatus


# Automatic Values

"""
Python can automatically assign automatic values to the members

enum.auto() as member values
_generate_next_value_ is the method

-> Default implementation results in sequential integer numbers

"""


class NumberExample(Enum):
    one = auto()
    two = auto()
    th3 = auto()


print(f"{NumberExample.one.value, NumberExample.two.value, NumberExample.th3.value}")


""" 
_generate_next_value (name, start, count, last_values)
args:
 name : the name of the member
 start: (only actually used in functional creation - not covered in this course)
 count: the number of already created (be careful with aliases)
 last_values : list of previous values (preceding values)
 
 returns:
    value to be assigned to member

Overriding:
    the default implementation of _generate_next_value_ generates sequential integer numbers
    -> be careful mixing auto() and your own values
    -> safer not do it
    
"""


# CODING
class StateOne(Enum):
    waiting = auto()
    started = auto()
    finished = auto()


for member in StateOne:
    print(member.name, member.value)


class StateTwo(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values):
        print(f"name={name}. start={start}, count={count}, last_values={last_values}")
        return 100
    a = auto()
    b = auto()
    c = auto()


for mem in StateTwo:
    print(member.name, member.value)

import random


class StateThree(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values):
        print(f"name={name}. start={start}, count={count}, last_values={last_values}")
        while True:
            new_value = random.randint(1, 10)
            if new_value not in last_values:
                return new_value

    a = auto()
    b = auto()
    c = auto()
    d = auto()

for mem in StateThree:
    print(mem.name, mem.value)


class StateFour(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values):
        print(f"name={name}. start={start}, count={count}, last_values={last_values}")
        return name.title()

    WAITING = auto()
    STARTED = auto()
    FINISHED = auto()

for m in StateFour:
    print(m.value, m.name)


# using lower case
class NameAsString(Enum):
    def _generate_next_value_(name: str, start: int, count: int, last_values):
        print(f"name={name}. start={start}, count={count}, last_values={last_values}")
        return name.lower()


class Enum1(NameAsString):
    A = auto()
    B = auto()
print(list(Enum1))


class Enum2(NameAsString):
    WAITING = auto()
    STARTED = auto()
    FINISHED = auto()
print(list(Enum2))