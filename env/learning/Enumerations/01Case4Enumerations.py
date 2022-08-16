from enum import Enum


# How to deal with collections of related constants

red = 1
green = 2
blue = 3

colors = (red, green, blue)

# in the code we can do using

pixel_color = {'red':1, 'green': 2, 'blue': 3}

# retrieve red
print(f"we can retrieve color by {pixel_color['red']}")
print(f"we can retrieve color by {pixel_color['red']}")

# downsides
# from the first statement of print:
print(f"we can retrieved color by {pixel_color['red']} is actually "
      f"red in the dict_variable")
print(f"we can retrieved color by {pixel_color['red']} using integer, is pixel_color position 1"
      f"really, what happens when we introduced or add a new color")

"""
 We want a immutable collection of related constant members:
 -> have unique names (that may have meaning)
 -> have an associated constant values
 -> unique associated values
 -> operators such as red * 2 or RED < GREEN are not even allowed
    -> lookup member by name
    -> lookup member by value

"""


# May be use a class
class Colors:
    RED = 1
    GREEN = 2
    BLUE = 3


# We want retrieve value of RED
print(Colors.RED)

# We want to check whether attribure RED exists in COLORS class
print(f"does red exist: {hasattr(Colors, 'RED')}")

# We want to get color 'RED'
print(f"i want color 'red': {getattr(Colors, 'RED')}")


based_on_value = """
    -> how do we look up based on value?
    -> how do we iterate the members?
    -> we can , but is order presevered
    -> still cannot guarantee uniqueness of values
    
 """

# Aliases
"""
Some times we want multiple symbols to refer to the same thing

"""
# Enumerations
"""
Enumerations was introduced in PEP 435 

we have module enum module
-> Enum type
-> specialised enumerations: IntEnum, Flag and IntFlag
"""


"""

# Color is now called Enumeration
print(f"Enumeration member is now {Color.RED}")

# type (Color.RED)
print(f"{type(Color.RED)} is the type")
print(f"{isinstance(Color.RED, Color)} is the instance")

"""

# Equality and membership
"""
member equality is done using identity `is` (but == works too) 


note that member and its associated value are not equal.
Enumeration members are always hashable.

-> can be used as keys in dictionaries
-> can be used as elements of a set

Enumerating Members:
    enumerations are iterables
    we use `list` using list(Color) -> [Color.RED, Color.GREEN, Color.BLUE]
    
Enumerations have __members__ property.

Constant Members and Constant Values:
    Once an enumeration has been declared.
    -> member list is immutable 
    -> members values are immutable
    -> cannot be subclassed (extended via inheritance)
        -> unless it contains no members
        
    
"""


# Coding (Basics of Enumerations)
# Terminology: Create a class with Enum class
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Status(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'


class UnitVector(Enum):
    V1D = (1, )
    V2D = (1, 1)
    V3D = (1, 1, 1)

# check the status of the pending
print(Status.PENDING)

# checking the type
print(type(Status.PENDING))

# check the instance
print(f" instance of Status {isinstance(Status.PENDING, Status)}")

# check the name and value
print(f"name = {Status.PENDING.name}, value = {Status.PENDING.value}")

# check the UnitVector v3d value
print(f" V3D = {UnitVector.V3D.value}")

# instantiate
a = Status.PENDING

# comparison:
print(f"comparison of `a` is {a is Status.PENDING} and its in `Status.PENDING` ")


class Constants(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


# Enum classes are callable.
#print(Status(''))


class Person:
    def __getitem__(self, val):
        return f"__getitem__({val}) called...."


p = Person()

try:
    p['some value']
except ValueError as ex:
    print(ex)

# check whether class has attribute '__getitem__'
print(f'does Status class as __getitem__property {hasattr(Status, "__getitem__")}')

# check the member of Status
print(f" {Status['PENDING']}")

# enumerations values are hashable.
class Person:
    __hash__ = None


p = Person()

try:
    print(hash(p))
except TypeError as ex:
    print(ex)


class Family(Enum):
    person_1 = Person()
    person_2 = Person()


print(Family.person_1)

family_dic = {
    Family.person_1: 'person 1',
    Family.person_2: 'person 2'
}

# iterable
print(f" is Status class having __iter__? {hasattr(Status, '__iter__')}")

for x, member in enumerate(Status):
    print(f"member {x} = {repr(member)}")

print(list(Status))


class EnumBase(Enum):
    # ONE = 1
    pass

class EnumExt(EnumBase):
    TWO = 2

