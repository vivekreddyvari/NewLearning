import ctypes

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

print(f"is p1 a p2:{p1 is p2}, yes id(p1) {id(p1)}= id(p2) {id(p2)} ")
print(ref_count(id(p1)))

del p2
print(ref_count(id(p1)))
p1_id = id(p1)
print(ref_count(p1_id))

del p1
print(p1_id)

