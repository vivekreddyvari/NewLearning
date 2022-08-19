# Descriptors

"""
The Underspinning mechanism for properties, methods, slots and even functions!
non-data vs data descriptors
writing custom descriptors
avoiding common storage pitfalls
weak references and weak dictionaries

"""

"""
Suppose we want a Point2D class whose coordinates must always be integers
    -> plain attributes for x and y cannot guarantee this.
    -> instead we can use a property with getter and setter methods

"""
# Lets implement x first


class Point2D:
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = int(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = int(value)

    def __init__(self, x,y):
        self.x = x
        self.y = y

""" 
The above Point2D has repetitive code, in order to avoid this, descriptors were introduced

To break the above code into simpler:
    -> Step1: Create a IntegerValue class
    -> Step2: Create x, y as class instances
    
"""


class IntegerValue:
    def get(self):
        return self._value

    def set(self, value):
        self._value = int(value)

    def __init__(self, value):
        if value:
            self.set(value)


# Now create a class Point2D1
class Point2D1:
    # Define instantiating class
    x = IntegerValue(1)
    y = IntegerValue(2)

#  Descriptor protocols
"""
There are 4 method that makes descriptor protocols - they are not all required
 - > __get__    used to get an attribute value p.x
 - > __set__    used to set an attribute value p.x = 100
 - > __delete__ used to delete an attribute del p.x
 - > __set_name__ new in python 3.6 
"""

# Two categories of descriptors
"""
 Non-data descriptor -> those implement __get__ only
 data descriptor -> thoese implement __set__ and/or __delete__
 
"""

# Non-data Descriptor
"""
__get__ method

"""
from datetime import datetime


class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()

l = Logger()

print(l.current_time) # calls __get__



