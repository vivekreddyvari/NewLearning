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
