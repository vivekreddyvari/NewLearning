import enum
from enum import Enum
import enum


# Recall that members are guaranteed to be unique:
"""
So this should not work:

We still have unique members but we now also have aliases


    
"""


# Example of Alias in an Enumeration:
class ExampleColors(Enum):

    RED = 1
    CRIMSON = 1 # Alias of RED
    CARMINE = 1 # Alias of RED
    BLUE = 2
    AQUAMARINE = 2 # Alias of BLUE


# Instantiate
color = ExampleColors

# Lets checks the members of colors
print(f"The members of the colors are: {color.__members__}")

# Let's check which color points to which one (alias)
print(f"is `crimson` a `red` yes it is {color.CRIMSON}")
print(f"is `carmine` a `red` yes it is {color.CARMINE}")
print(f"is `aquamarine` a `blue` yes it is {color.BLUE}")

# Let's check with comparison
print(f"is crimson = red ({color.CRIMSON is color.RED})")
print(f"is aquamarine = blue ({color.AQUAMARINE is color.BLUE})")

# Lookups
"""
Lookups with aliases will always return the `master` member
e.g.
color(1) -> color.red
color['crimson'] -> color.red

"""

# Containment:
"""
Works similar to Lookup
e.g. color.crimson in color -> True
"""

# Iterating ALias
"""
list(Color) -> color.red, color.blue
"""


# Ensuring Unique Values:
"""
we may want to guarantee that our enumerations do not contain aliases (unique values)
we could just be careful writing our code
or use the @enum.unique decorator
"""

class ExColorOne(Enum):
    red = 1
    crimson = 1
    carmine = 1
    blue = 2
    aquamarine = 2


@enum.unique # avoid duplicates
class ExColorTwo(Enum):
    red = 1
    #crimson = 1
    #carmine = 1
    blue = 2
    #aquamarine = 2


# CODING - ALIAS
class NumSides(enum.Enum):
    Triangle = 3
    Rectangle = 4
    Square = 4
    Rhombus = 4
    Isoceles = 3

# by Key
print(f"is Rectangle a Square {NumSides.Rectangle is NumSides.Square}")

# by value
# print(f"retrieve 4 sides {NumSides[3]}")

# by key
print(f"square as key {NumSides['Square']}")


class Status(Enum):
    read = 'ready'

    running = 'running'
    busy = 'running'
    processing = 'running'

    ok = 'ok'
    finished_no_error = 'ok'
    ran_ok = 'ok'

    errors = 'errors'
    finished_with_error = 'errors'
    errored = 'errors'


print(f'lets check list of Status {list(Status)}')

# decorator to avoid duplicates @enum.unique

