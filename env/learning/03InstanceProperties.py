import ctypes

# Using Instance Properties

"""
-> We know the instance we are dealing with in both __get__ and __set__
    -> Could maybe store it in the instance dictionary?

that might work...
    but remember __slots__?

-> We're not guaranteed to have an instance dictionary available
-> even if we were, what symbol to use? Might overwrite an existing attribute...
-> so maybe we use a dictionary that's local to the data descriptor instance.
    -> key = object -> problem if object is not hashable
    -> value = value

Assuming our objects are hashable...
-> Create a dictionary in the data descriptor instance (e.g. in IntegerValue Instance)
-> when using__set__ save the value in the dictionary using instance as a key
=> when using __get__ lookup the instance in the dictionary and return the value

"""


class ExIntegerValue:
    def __init__(self):
        self.data = {}

    def __set__(self, instance, value):
        self.data[instance] = int(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance)


# Instantiate and call
class ExPoint2D:
    x = ExIntegerValue()
    y = ExIntegerValue()

eP = ExPoint2D() #Reference count is 1

print(eP.x)

eP.x = 100
print(eP.x, eP.__dict__)

del eP


# Coding
# Using as instance Properties.

class C1IntegerValue:
    def __set__(self, instance, value):
        instance.stored_value = int(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, 'stored_value')


class C1Point1D:
    x = C1IntegerValue()

c_p1, c_p2 = C1Point1D(), C1Point1D()

c_p1.x = 10.1
c_p2.x = 20.2

print(c_p1.x, c_p2.x)

print(c_p1.__dict__)
print(c_p2.__dict__)


class C1Point2D:
    x = C1IntegerValue()
    y = C1IntegerValue()


coding_p1 = C1Point2D()
coding_p1.x = 10.1
print(coding_p1, end='\n\n')
print(coding_p1.__dict__, end='\n\n')

coding_p2 = C1Point2D()
coding_p2.x = 20.1
print(coding_p2, end='\n\n')
print(coding_p2.__dict__, end='\n\n')


# class Integer
class C2IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


# class Point2D redefined with new x and y
class C2Point2D:
    x = C2IntegerValue('x')
    y = C2IntegerValue('y')

# create Instantiating
coding1_p1, coding1_p2 = C2Point2D(), C2Point2D()

coding1_p1.x = 10.3
coding1_p1.y = 20.1

print(coding1_p1.__dict__, end='\n\n')
print(coding1_p2.__dict__, end='\n\n')

coding1_p2.x = 100.1
coding1_p2.y = 200.1

print(coding1_p2.__dict__, end='\n\n')


# class Integer - Descriptor Instance with memory leak
class C3IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.values.get(instance, None)


class C3Point2D:
    x = C3IntegerValue()
    y = C3IntegerValue()


p1 = C3Point2D()
p2 = C3Point2D()

p1.x = 10.1
p1.y = 20.2
print(p1.x, p1.y, end='\n\n')
print(C3Point2D.x.values)

p2.x = 100.2
print(p2.x, end='\n\n')

p2.y = 200
print(C3Point2D.y.values)

# This approach has some problem with memory for example

hex(id(p1))

del p1

print(C3Point2D.x.values, end='\n\n')

code_p1 = list(C3Point2D.x.values.keys())[0]

print(f' we can observer, that del of p1 is not deleted and code_p1={code_p1}', end='\n\n')


def ref_count(address):
    return ctypes.c_long.from_address(address).value

code_test_p1 = C3Point2D()
code_test_p1_id = id(code_test_p1)

print(ref_count(code_test_p1_id))

code_test_p1.x = 100.1
print(ref_count(code_test_p1_id))

print(f"Lets us check whether code_test_p1={'code_test_p1' in globals()} in globals")

del code_test_p1

print(f"Lets us check whether code_test_p1={'code_test_p1' in globals()} in globals after deletion")