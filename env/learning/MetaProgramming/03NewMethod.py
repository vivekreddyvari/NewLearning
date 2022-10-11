import pdb
pdb.set_trace()

# the __new__ method
"""

constructing instances of a class
-> call the class ex.Person('Guido) -> classes are callable
                                    -> how back to that later

-> the new class instance is created.
    (and initialized in some ways)
-> the __init__ method is called (bound to the new object)
    -> after the instance has been created
    -> gives us a "hook" to customize the initialization

-> but how is the new instance actually created?

the __new__ method
 -> object implements the __new__ method
    -> it is a default implementation of __new__
    -> used in the creation of instance of any class

-> can be called directly

    example:
    class Person:
        def __init__(self, name):
            self.name = name

    # create an instance with new method
    p = object.__new__(Person)
        -> p is a new object, an instance of the Person
        -> __init__ is not called.
            -> do it ourselves. p.__init__('Raymond')

Working of __new__ method

The __new__ method:
    object.__new__(class, *args, **kwargs)
        -> it is a static method
            -> not bound to object
            -> class is the symbol for the class we want to instantiate
        -> accepts *args, **kwargs
        -> signature must match __init__ of class
        -> but it just ignores these arguments
        -> returns a new object of type class
    -> so we override __new__ in our custom classes
    -> should return a new object
        -> should be an instance of the class
        -> but does not have to be

# Overriding the __new__ method

-> type we do something before / after creating the new instance.
    -> delegating actual creation to object.__new__
    -> in practice we use super().__new__
    -> ensures inheritance works properly

class Person:
    def __new__(cls, name, age):
         # can do things here
    # create the object we want to return
    instance = object.__new__(cls)

    # more code here

    # and finally reutnr the object we want
    return instance

HOw is __new__ method called?
 it is called by Python when we call the class

Person('Guido')
python calls __new__(Person, 'Guido')

    -> __new__ returns an objects
        -> if that object is of the same type as the one 'requested'
            -> new_object.__init__('Guido') is called
    -> new object is returned from call

__new__ is a static method

-> done implicitly for us by Python

class Person:
    @static Method
    def __new__(cls, name):
        return super().__new__(cls)


"""


# Coding
class PointExampleOne:
    pass

# Instantiate
pOne = PointExampleOne()

# Dict and Type of pOne
print(f" {pOne.__dict__}, {type(pOne)}")

# Create a new object using __new__ method
pOne_One = object.__new__(PointExampleOne)

#
print(f" {pOne_One.__dict__}, {type(pOne_One)}")


def my_func(value):
    if value == 5:
        return ["Python"]
    else:
        yield from range(value)

print(list(my_func(5)))

# talk

