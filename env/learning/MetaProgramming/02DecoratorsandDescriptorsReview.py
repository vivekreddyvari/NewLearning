from functools import wraps

# Decorator and Descriptors - Review


# write a debug method used in the code
def debugger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print(f"{fn.__qualname__}", args, kwargs)
        return fn(*args, **kwargs)
    return inner


@debugger
def func_1(*args, **kwargs):
    pass


@debugger
def fun_2(*args, **kwargs):
    pass

print(func_1(10, 20, kw='a'))
print(fun_2(10))


# Descriptor - to do Dry code
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.x, p.y)
print(p.__dict__)


# set and get values
class IntegerField:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print("__get__ called")
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Must be an integer')
        instance.__dict__[self.name] = value
        print("__set__ called")


class PointExampleOne:
    x = IntegerField()
    y = IntegerField()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pOne = PointExampleOne(10, 20)
print('\n\n\n')
print(pOne.x, pOne.y)

try:
    pOne.x = 10.5
except TypeError as ex:
    print(repr(ex))
