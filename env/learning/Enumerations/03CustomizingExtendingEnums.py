from enum import Enum

# Customizing / Extending Enums - Lecture.

# Customizing:
"""
Enums are classes
 class attribute become instances of that class -> members

we can define functions in the enumeration class.
-> become bound methods when called from a member (instance of the class)

-> Custom Methods
-> implement dunder methods
__str__ __repr__ __eq__ __lt__ etc

Member Truthyness
 by default, every member of an enum is truthy
 -> irrespective of the member value



"""


# class with bool, that cannot be overriden
class State(Enum):
    READY = 1
    BUSY = 0

print(f"what is bool of READY: {bool(State.READY)} returns TRUE"
      f" which is correct")
print(f"what is bool of BUSY: {bool(State.BUSY)} returns "
      f"FALSE which is incorrect")


# so we can implement __bool__ method to override the above behaviour
class StateOne(Enum):
    READY = 1
    BUSY = 0

    def __bool__(self):
        return bool(self.value)

print(f"what is bool of READY: {bool(StateOne.READY)}")
print(f"what is bool of BUSY: {bool(StateOne.BUSY)}")


# Extending Enums
"""
 Enumerations are classes -> they can be extended (sub-classsed)
 
 BUT... only if they do not contain any members
    -> Cannot create a partial enum with some members and extended it with more members
    -> might seem limiting, but not really
    -> create a base enum with functionality (methods)
    -> use it as abase class for other enumerations that define their members.
"""


# Coding
class ColorOne(Enum):
    red = 1
    green = 2
    blue = 3

    def purecolor(self, value):
        return {self.value}

print(f"The repr of ColorOne without REPR {ColorOne.red}")


# custom representation.
class ColorTwo(Enum):
    red = 1
    green = 2
    blue = 3

    def __repr__(self):
        return f"{self.name} ({self.value})"

print(f"The repr of ColorTWO is now changed {ColorTwo.red}")


class NumberOne(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, NumberOne) and self.value < other.value

print(f"{NumberOne.ONE < NumberOne.TWO}")
print(f"{NumberOne.ONE > NumberOne.TWO}")


class NumberTwo(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, NumberOne) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, NumberTwo):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        return False

print(NumberTwo.ONE is NumberTwo.ONE, NumberTwo.ONE == NumberTwo.ONE)
print(NumberTwo.ONE == 1)
print(NumberTwo.ONE == 1.0)


# hashablity
class NumberThree(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, NumberThree) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, NumberThree):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        return False

    def __le__(self, other):
        return isinstance(other, NumberThree) and self.value <= other.value

print(NumberThree.ONE >= NumberThree.TWO)

# OR import total_ordering from functools
try:
    from functools import total_ordering
except ImportError as ex:
    print(ex)


@total_ordering
class NumberFour(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, NumberFour) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, NumberFour):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        return False

print(NumberFour.ONE >= NumberFour.TWO)


class Phase(Enum):
    READ = 'ready'
    RUNNING = 'running'
    FINISHED = 'finished'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Phase):
            return self is other
        elif isinstance(other, str):
            return self.value == other
        return False

    def __lt__(self, other):
        ordered_items = list(Phase)
        self_order_index = ordered_items.index(self)
        if isinstance(other, Phase):
            other_order_index = ordered_items.index(other)
            return self_order_index < other_order_index
        if isinstance(other, str):
            try:
                other_member = Phase(other)
                other_order_index = ordered_items.index(other)
                return self_order_index < other_order_index
            except ValueError:
                return False

print(Phase.READ == 'ready')
print(Phase.READ < Phase.RUNNING)
print(Phase.READ < 'running')


class StateTwo(Enum):
    READY = 1
    BUSY = 0

    def __bool__(self):
        return bool(self.value)


state = StateTwo.READY
if state:
    print('system is processing...')
else:
    print('system is busy...')


class Dummy(Enum):
    A = 0
    B = 1
    C = ''
    D = 'python'

    def __bool__(self):
        return bool(self.value)

print(bool(Dummy.A), bool(Dummy.B), bool(Dummy.C), bool(Dummy.D))


# Subclass
class ColorThree(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


try:
    class ColorAlpha(ColorThree):
        ALPHA = 4
except TypeError:
    print('cannot extend enumerations')


class ColorBase(Enum):
    def hello(self):
        return f"{str(self)} says hello"


class ColorFour(ColorBase):
    RED = 1
    GREEN = 2
    BLUE = 3

print(ColorFour.RED.hello())


@total_ordering
class OrderedEnum(Enum):
    """ Create an ordering based on the member values
    so member values have to support rich comparisons """

    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented


class NumFive(OrderedEnum):
    ONE = 1
    TWO = 2
    THR = 3


print(NumFive.ONE < NumFive.TWO)
print(NumFive.THR >= NumFive.TWO)

# http module
from http import HTTPStatus
print(type(HTTPStatus))
print(list(HTTPStatus))


class AppStatus(Enum):
    OK = (0, 'No Problem')
    FAILED = (1, 'Crap!')

    @property
    def code(self):
        return self.value[0]

    @property
    def phrase(self):
        return self.value[1]


print(AppStatus.OK.value, AppStatus.OK.name, AppStatus.OK.phrase)


class AppStatusOne(Enum):
    OK = (0, 'No Problem')
    FAILED = (1, 'Crap!')

    def __new__(cls, member_value, member_phrase):
        # print(cls, member_value, member_phrase)
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member

print(AppStatusOne.OK.value, AppStatusOne.OK.name, AppStatusOne.OK.phrase)
print(AppStatusOne(0), AppStatusOne(1))


class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member


class AppStatusThree(TwoValueEnum):
    OK = (0, 'No Problem')
    FAILED = (1, 'Crap!')

print(AppStatusThree.FAILED.value, AppStatusThree.FAILED.name, AppStatusThree.FAILED.phrase)