from datetime import datetime
"""
Getter : __get__ method
    -> get the attribute value
    How __get__ is called
        -> signature in __get__(self, instance, owner_class)
    can return different values
        -> called from class
        -> called from instance

Setter : __set__ method
    -> signature = self, instance, value
    -> self: just like the __get__ this references the descriptor instance, like any regular method
    -> instance: the instance the __set__ method was called from
    -> value : the value we want to assign to the attribute

You 'll notice there is no owner_class like we have in the __get__ method
-> setter (and deleters) are always called from instances
 
"""


# Caveat with set and delete (and get)
"""
class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    current_time = TimeUTC()

# create the instance and call

l1 = Logger()
l2 = Logger()
"""


# what happens when we call instance
"""
 -> any instance of the Logger will be referencing the same instance of TimeUTC
    -> the same instance of TimeUTC is shared by all instances of Logger
     
"""

# Caveat with set and Delete (and get)

"""
    -> But what happens when we have to store and retrieve data from instance?
    Supper IntegerValue is a data descriptor
    
"""


# Coding
# 01 Getter and setter
class TimeUTC1:
    def __get__(self, instance, owner_class):
        print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
        return datetime.utcnow().isoformat()


class Logger1:
    current_time = TimeUTC1()


class Logger2:
    current_time = TimeUTC1()

getattr(Logger1, 'current_time')

print(Logger1.current_time)

print(Logger2.current_time)


l1 = Logger1()
print(hex(id(l1)))
print(l1.current_time)

l2 = Logger2()
print(hex(id(l2)))
print(l2.current_time)


# Redefining the TimeUTC
class TimeUTC2:
    def __get__(self, instance, owner_class):
        if instance is None:
            print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
            return self
        else:
            print(f'__get__ called, self={self}, instance={instance}, owner_class={owner_class}')
            return datetime.utcnow().isoformat()


class Logger3:
    current_time = TimeUTC2()


print('\n\n')
getattr(Logger3, 'current_time')
print(Logger3.current_time)

l3 = Logger3()
print(hex(id(l3)))
print('\n')

print(l3.current_time)

# Careful When
class CountDown:
    def __init__(self, start):
        self.start = start + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.start -= 1
        return self.start


class Rocket:
    countdown = CountDown(10)

rocket1 = Rocket()
rocket2 = Rocket()

print(rocket1.countdown)
print(rocket2.countdown)
print(rocket1.countdown)

print('\n SET METHOD')


class IntegerMethod:
    def __set__(self, instance, value):
        self._value = value
        # print(f'__set___called, instance={instance}, value ={value}')

    def __get__(self, instance, owner):
        if instance is None:
            #print('__get__ called from class')
            return self
        else:
            # print(f'__get__called, instance={instance}, owner_class={owner}')
            return self._value


class Point2D:
    x = IntegerMethod()
    y = IntegerMethod()

print(Point2D.x)

p = Point2D()
# print(p.x)
p.x = 1.1
p.y = 2.2
print(p.x, p.y)
