# Property value lookup Resolution:

"""
Interesting Thing:
    -> Class can have a property (descriptor) called x
    -> It can have an instance dictionary __dict__
        -> that dictionary may contain a key, also called x

    what happesn when we do this:
        obj.x
        or
        obj.x = value
answer:
it depends...
    - on whether descriptor is a data or non-data descriptor

    data descriptors  [both __get__ and __set__ are defined]
        -> always override the instance dictinary [by default - can override this behaviour]

if non-data descriptors
 -> only (__get__ is defined, and potentially __set_name__)
 -> looks in the instance dictionary list
 -> if not present, uses the data descriptor


"""


# Coding
# Property Lookup Resolution
# data descriptor or not?
class InterValueEx1:
    # data descriptor (__get__ and __set__) are defined
    def __set__(self, instance, value):
        print('__set__ called....')

    def __get__(self, instance, owner_class):
        print('__get__ called...')


class Point:
    x = InterValueEx1()

# Instantiate with p
p = Point()

# Lets set the value
p.x = 100
print(f" {p.x} is the value ")

# Lets check the dictionary
print(f"{p.__dict__}")

# lets set the value in dictinary
p.__dict__['x'] = 'Hello'

# Lets check the dictionary
print(f"{p.__dict__}")
print(f" {p.x} is the value ")


# Non-Data Descriptor
class TimeUTC:

    def __get__(self, instance, owner_class):
        print("__get__ called....")

    def __del__(self):
        print('__del__ called...')
class Logger:
    current_time = TimeUTC()

l = Logger()
print(f"{l.current_time}")

# check the dictionary of l
print(f"{l.__dict__}")

# lets set the value in dictinary
l.__dict__['current_time'] = 'Hello'

# check the dictionary of l
print(f"{l.__dict__}")
print(f"{l.current_time}")

del l.__dict__['current_time']


class ValidString:

    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} not long enough')

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f'called __get__ {self.property_name}')
        return instance.__dict__.get(self.property_name, None)

    #def __del__(self):
        #print('__del__ is called')


# create class PErson
class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)

person = Person()
person.first_name = 'Jak'
person.last_name = 'vu'
print(f" {person.__dict__} is from {Person}")
del person

class ValidStringEx:

    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        print(f"__set__ called")
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} not long enough')
        setattr(instance, self.property_name, value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print(f'called __get__ {self.property_name}')
        return instance.__dict__.get(self.property_name, None)


class Person2:
    name = ValidStringEx(1)


person1 = Person2
person1.name = 'Alex'
print(person1.name)

