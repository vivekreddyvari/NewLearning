import types

# Function and Descriptor"
"""
Function are objects that implement (non-data) descriptor protocol that __get__ method

"""


def add(a, b):
    return a + b

print(f" {hasattr(add, '__get__')}, {type(add)} are non-data descriptors")
print(hasattr(add, '__set__'))


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"{self.name} says hello"

# Let's check if a Person class is non-data descriptors?
print(f"is `class Person` a non-data descriptor {Person.say_hello}, "
      f"{hasattr(Person.say_hello, '__get__')}")

# Let's check from the instance
personOne = Person('Alex')
print(f"is `instance: personOne of"
      f"` a non-data descriptor {hasattr(personOne.say_hello, '__get__')}, {personOne.say_hello}")

bound_method = Person.say_hello.__get__(personOne, Person)
print(f"{bound_method}")

f1 = personOne.say_hello
f2 = personOne.say_hello

print(f1, f2)
print(f1 is f2)
print(bound_method())

class MyFunc:

    def __init__(self, func):
        self._func = func

    def __get__(self, instance, owner_class):
        if instance is None:
            print('__get__ called from class')
            return self._func

        else:
            print(f"__get__ called from instance")
            return types.MethodType(self._func, instance)


def hello(self):
    print(f"{self.name} says hello!")


class Person:
    def __init__(self, name):
        self.name = name

    say_hello = MyFunc(hello)


p1 = Person("Alex")
print(p1.say_hello)
print(p1.say_hello.__func__)
print(p1.say_hello())



