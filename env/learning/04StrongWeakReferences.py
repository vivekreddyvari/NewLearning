import ctypes
import weakref

# STrong and WEak Reference

# Strong references
"""
p1 = Person()   -> is a strong reference
p2 = p1         -> is a strong reference

de1 p2  - > There is still a strong reference (p2) to the object
        -> Object is still alive, so python does not garbage collect

del p2 -> no more strong references to object
       -> object will be garbage collected by Python

That's the problem we faced in our data descriptor in previous tutorial 03InstanceProperties.py

"""

# Weak References
"""
There is another type of reference in Python -> Weak Reference
    think of it as a reference to an object that does not affect the reference count as far as the 
    memory manager is concerned.
    
    p1 is object which is strong referenced.
    p2 = p1, here p2 is weak reference as it first referred to p1 and later to object
    
    -> del p1 -> No More (strong) reference to object
              -> Object is garbage collected
              -> p2 is dead
    -> So for our data descriptor instead of storing the object as key
        -> store a weak reference to the object
    
    In Python we have module = weakref module
    
    p1 = Person() -> P1 has strong reference to the object
    p2 = weakref.ref(p1)     -> P2 is an (other) object that contains a weak reference
    

    -> p2 is a callable
    p2() -> Returns the original object
         -> or None if the object has been garbage collected
         
    careful p3=p2()
         -> You just created a strong reference to the object
         
    
Dictionaries of Weak Reference:
so we'll create  a dictionary of weak references( for our keys)
    -> weakref has a WeakKeyDictionary to do just that!
    
    p1 = Person() - > strong reference to the Person instance
    d = WeakKeyDictionary()
    d[p2] = 'some value' -> a weak reference is used for the Person instance
    
    del p2  -> no more strong references -> garbage collected
    
        -> item is automatically removed from weak key dictionary
        (so be carefully if you're iterating over the dictionary views if that happens
        during the iteration!
         we won't need to, so won't be a problem for our use-case)
         
    
"""


# Coding
# Counter to the references.
def ref_count(address):
    return ctypes.c_long.from_address(address).value


class CodeOnePerson:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

p1 = CodeOnePerson('Guido')
p2 = p1

print(f"is p1 a p2?:{p1 is p2}, yes id(p1)= {id(p1)} and id(p2)= {id(p2)} ")
print(ref_count(id(p1)))

del p2
print(ref_count(id(p1)))
p1_id = id(p1)
print(ref_count(p1_id))

del p1
print(ref_count(p1_id))
print(p1_id, "is a garbage collector reference keeps changes ")

p1_I = CodeOnePerson("Van Russum")
p1_id_I = id(p1_I)

print(ref_count(p1_id_I), "Before referencing")

p2_I = p1_I
print(ref_count(p1_id_I), "After referencing")

weak1_I = weakref.ref(p1_I)
print(ref_count(p1_id_I), "Checking the weak reference " )

print(weak1_I, "The weak reference ")
print(hex(p1_id_I), "the memory address of weak reference")

print(weak1_I(), "Weak reference ")



del p1_I
print(ref_count(p1_id_I), "still there ?")

print(weak1_I, "check it is still alive")

del p2_I
print(ref_count(p1_id_I), "still there ?")
print(weak1_I, "check it is still alive? ")

l = [1, 2, 3]
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)

# Data descriptors as keys, as it will not stop from being destroyed.
p1 = CodeOnePerson("Guido")

d = weakref.WeakKeyDictionary()

print(ref_count(id(p1)), "How many Weak references")

n = {p1: "Guido"}
print(ref_count(id(p1)), "Checking how references the p1 has")

# Del
del n
print(ref_count(id(p1)), "Now how many weak references does `p1` has?")

d[p1] = "Guido"
print(ref_count(id(p1)), "after using weak reference dictionary, and `p1` has?")
print(weakref.getweakrefcount(p1), "To know how many weak reference it has")

d2 = weakref.WeakKeyDictionary()
d2[p1] = "Guido"

print(ref_count(id(p1)), weakref.getweakrefcount(p1), "How many weak references does p1"
                                                      "as referred and using weak ref dict?")

print(p1.__weakref__, "Python referencing Linked_List")
print("check the reference number ", hex(id(p1)))
print("How many key weak references does p1 has", list(d.keyrefs()))

# Deletion one-only strong reference.
del p1
reference_count = ''
if len(list(d.keyrefs())) == 0:
    reference_count = 'Empty'
print(f'How many key weak references does p1 has now, Lets check and p1 is {reference_count} and it is {list(d.keyrefs())}')


class CodeTwoPerson:
    def __init__(self, name):
        self.name = name


person1 = CodeTwoPerson("Person1")

if hash(person1) != 0: print(f"Is the person1 hashable, {hash(person1)}")


class CodeThreePerson:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, CodeThreePerson) and self.name == other.name


person3_I = CodeThreePerson("Fred")
person3_II = CodeThreePerson("Fred")

if person3_I == person3_II: print(f"yes Person3_I = person3_II is {person3_I == person3_II}")

try:
    hash(person3_I)
except Exception as ex:
    print(ex)


class CodeFourPerson:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, CodeFourPerson) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

person4_I = CodeFourPerson("Fred")
person4_II = CodeFourPerson("Fred")

if person4_I == person4_II: print(f"yes Person4_I = person4_II is {person4_I == person4_II}")

try:
    hash(person4_I)
except Exception as ex:
    print(ex)

d[person4_I] = "Test"
if list(d.keyrefs()) != ' ': print(f"{list(d.keyrefs())}")

del person4_I

if len(list(d.keyrefs())) != 0: print(f"{list(d.keyrefs())}")


