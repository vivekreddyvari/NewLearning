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
"""