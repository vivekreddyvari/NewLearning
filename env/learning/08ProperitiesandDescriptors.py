from numbers import Integral

# Properties and Descriptors

"""
property objects are data descriptors
    -> they have __get__, __set__ and __delete__ methods

    age = property(fget=get_age, fset=set_age)
    p.age -> calls __get__ -> in turn calls get_age(p)
    p.age = 10 -> calls __set__ -> in turn calls set_age(p, 10)

    if fset was not defined,
        -> calls __set__
        -> __set__ sees fset is not defined
        -> raises on attribute error (can't set attributes)
        
"""


# Coding
class PersonOne:

    @property
    def age(self):
        return getattr(self, '_age', None)

    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError(f'age: Must be an integer')
        if value < 0:
            raise ValueError(f'age must be a non_negative integer')
        self._age = value

pone = PersonOne()

try:
    pone.age = -10
except ValueError as ex:
    print(ex)

print(f'Dictinary of pOne is {pone.__dict__}')

# set age to 10
pone.age = 10
print(f'Dictionary of pOne is {pone.__dict__} after setting age to 10')


# without decorator
class PersonTwo:

    def get_age(self):
        return getattr(self, '_age', None)

    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError(f'age: Must be an integer')
        if value < 0:
            raise ValueError(f'age must be a non_negative integer')
        self._age = value

    age = property(fget=get_age, fset=set_age)

prop = PersonTwo.age

print(f" is __get__ there ?: {hasattr(prop, '__get__')} ")
print(f" is __set__ there ?: {hasattr(prop, '__set__')} ")
print(f" is __del__ there ?: {hasattr(prop, '__delete__')} ")

ptwo = PersonTwo()
ptwo.age = 10

print(f"Lets check ptwo:age is {ptwo.age}")


# class UTC
class TimeUTC:
    @property
    def current_time(self):
        return 'Current Time'


# instantiate to T
t  = TimeUTC()
print(f" is __get__ there ?: {hasattr(TimeUTC.current_time, '__get__')} ")
print(f" is __set__ there ?: {hasattr(TimeUTC.current_time, '__set__')} ")
print(f" is __del__ there ?: {hasattr(TimeUTC.current_time, '__delete__')} ")


class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable')
        self.fset(instance, value)


class PersonThree:
    def get_name(self):
        print('get_name called')
        return getattr(self, '_name', None)

    def set_name(self, value):
        print('set_name called...')
        self._name = value

    name = MakeProperty(fget=get_name, fset=set_name)


pthree = PersonThree()
pthree.name = 'Guido'

print(pthree.name)


# Decorator Approach.
class PersonFour:

    def age(self):
        return getattr(self, '_age', None)

    age = property(age)

    def set_age(self, value):
        if not isinstance(value, Integral):
            raise ValueError(f'age: Must be an integer')
        if value < 0:
            raise ValueError(f'age must be a non_negative integer')
        self._age = value

    age = age.setter(set_age)
