# The __set_name__ method

"""
    This is a very handy method that gets called(onc) when the descriptor is first instantiated
        -> that opens many opportunities:
            -> better for error messages    (include the name of attribute that raised the exception)
            -> useful application in descriptors used for validation
        -> Application
            -> Pretty typical application of using custom descriptors
                -> again, key here is re-usability

        Suppose we have some attributes in a non-slotted class that need to be validated each time they are set
            -> get property name from __set_name__
            -> __set__
                -> validate data
                -> if Ok, store data in instance dictionary, under the same name
                    -> wait a minute, does instance dictionary not shadow class attribute?
                        -> not always with descriptors.

"""


# Coding!
# Lets check how __set_name__ works,
# define validstring with set method
#   - Let the __set__ function return a print statment.
class ValidString:
    def __set__(self, owner_class, property_name):
        print(f"__set_name__: owner={owner_class}, property_name={property_name}")


# create a class PersonExample with name property calling validstring()
class PersonExample:
    name = ValidString()

# Instantiate, PythonFather with PersonExample()
PythonFather = PersonExample()

# Set the name to Guido
PythonFather.name = 'Guido'


# Lets check with property
class ValidStringExample:
    def __set__(self, owner_class, property_name):
        print(f"__set_name__: owner={owner_class}, property_name={property_name}")
        self.property_name = property_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f"__get__ called for property {self.property_name} of instance{instance}")


class PersonExampleOne:
    first_name = ValidStringExample()
    last_name = ValidStringExample()

PythonFatherOne = PersonExampleOne()

# set the name to Guido and Van Russum
PythonFatherOne.first_name = 'Guido'
PythonFatherOne.last_name = 'Van Russum'

# Print to get functions
print(PythonFatherOne.first_name, PythonFatherOne.last_name)


# Lets check with property with additional parameters
class ValidStringExampleTwo:
    def __init__(self, min_length=None):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a string")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.property_name} should be at least {self.min_length} characters")
        key = '_' + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        key = '_' + self.property_name
        return getattr(instance, key, None)


# Lets check with PersonExample
class PersonExampleTwo:
    first_name = ValidStringExampleTwo(1)
    last_name = ValidStringExampleTwo(2)

# Instantiate PersonExampleTwo
person2 = PersonExampleTwo()

# set the name
try:
    person2.first_name = 'Alex'
    person2.last_name = 'M'
except ValueError as ex:
    print(ex)


try:
    person2.first_name = 'Alex'
    person2.last_name = 'Martelli'
except ValueError as ex:
    print(ex)

print(f"Dictionary of PersonExampleTwo = {person2.__dict__}")


# Bank Account Example
class BankAccountExampleOne:
    apr = 10


# Lets check with property with additional parameters __set__ with property name
class ValidStringExampleThree:
    def __init__(self, min_length=None):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a string")
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f"{self.property_name} should be at least {self.min_length} characters")
        instance.__dict__[self.property_name] = value
        # setattr(instance, self.property_name, value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self

        # key = '_' + self.property_name
        return instance.__dict__.get(self.property_name, None)


class PersonExampleThree:
    first_name = ValidStringExampleThree(1)
    last_name = ValidStringExampleThree(2)

# Instantiate PersonExampleTwo
person3 = PersonExampleThree()

# set the firstname of person3
person3.first_name = 'ALex'

# print the dictionary
print(f"{person3.__dict__} and {person3.first_name}")