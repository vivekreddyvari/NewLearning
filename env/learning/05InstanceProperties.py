import weakref
import ctypes

# Outstanding problem

"""
Using id(instance) as the key
still has a drawback
    -> if an object is finalized, the corresponding entry still remains in the dictionary
    -> (a big advantage of using weakkeydictinary)
    -> unnecessary clutter
    -> potential risk if id is re-used.
    -> but at least we don't maintain strong reference to object

"""

# Final Approach:
"""
weakref.ref -> callback functionality
            -> automatically calls a custom function when the object is being finalized
        
        -> use regular data dictionary
            -> use id(instance) as key
            -> use (weak_ref, value) as callback function
                -> for each weak_ref register a callback function
                -> callback function will remove dead entry from dictionary
        we can now implement data descriptors that:
         -> have instance specific storage.
         -> do not use the instance itself for storage(__slots__problem)
         -> handle non-hashable objects
         -> keep the data-storage clean
        
"""


# Coding:
class IntegerValueEx1:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)


# On hashable objects/classes
class IntegerValueEx2:
    def __init__(self):
        self.values = weakref.WeakKeyDictionary()

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)


class PointEx1:
    x = IntegerValueEx2()


p = PointEx1()
print(f' The Hex reference number of the point(`p`) =  {hex(id(p))}')

# set the point to 100
p.x = 100.1
print(f'The value of `p` is {p.x}, and reference of the `p` is  {PointEx1.x.values.keyrefs()}')

# deletion of p
del p
print(f'The references of `p` after deletion is, {PointEx1.x.values.keyrefs()}')


# Non Hashable classes
class IntegerValueEx3:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(id(instance))


class PointEx2:
    x = IntegerValueEx3()

    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, PointEx2) and self.x == other.x


p1 = PointEx2(10.1)

print(f"The value of point `p1` is {p1.x}")

# change the value of the p1
p1.x = 20.2
print(f"The value of point `p1` is {p1.x}")

# Reference of the p1 is
print(f"The value of point `p1` is {p1.x}, id={id(p1)}, reference is {PointEx2.x.values}")


def ref_count(address):
    return ctypes.c_long.from_address(address).value


# references count
print(f"The reference count of `p1` is {ref_count(id(p1))}")
p1_id = id(p1)

# del the reference
del p1
print(f"The reference count of `p1` after deletion is {ref_count(p1_id)}")
print(f"The value of point `p1` reference after deletion is {PointEx2.x.values}, "
      f"hence it is not deleted")


def obj_destroyed(obj):
    print(f"{obj} is being destroyed")


p2 = PointEx2(10.1)
weak2 = weakref.ref(p2, obj_destroyed)

del p2
print(f" is destroyed?, {weak2}")


# value is stored as weak ref of the object.
class IntegerValueEx4:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            values_tuple = self.values[(id(instance))]
            return values_tuple[1]

    def _remove_object(self, weak_ref):
        print(f" removing dead entry for {weak_ref}")


class PointEx3:
    x = IntegerValueEx4()


p1_II = PointEx3()
p2_II = PointEx3()

p1_II, p2_II = 10.1, 100.1

print(f"p1_II = {p1_II}, p2_II = {p2_II}")
p1_II_id = ref_count(id(p1_II))
p2_II_id = ref_count(id(p2_II))
print(f"Reference counts (p1_II, p2_II) = {p1_II_id, p2_II_id} before deletion")

del p1_II

print(f"Reference counts (p1_II, p2_II) = {p1_II_id, p2_II_id}  after deletion", end='\n\n')


# value is stored as weak ref of the object with reverse lookup.
class IntegerValueEx5:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            values_tuple = self.values[(id(instance))]
            return values_tuple[1]

    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]


class PointEx4:
    x = IntegerValueEx5()


p1_III = PointEx4()

# set the value of x in PointEx4
p1_III.x = 10.1

# Check the value
print(f"p1_III={p1_III.x}")

# Check the references
print(f"The references is/are: {PointEx4.x.values} before the deletion")

# Del the Point p1_III
del p1_III
print(f"The references is/are: {PointEx4.x.values} after the deletion")

# if we use __slots__ then weak_ref is gone.


class Person:
    __slots__ = 'name', '__weakref__'

person1 = Person()

# check whether weakref exists
print(f"Does Person1 has weak reference? {weakref.ref(person1)}", end='\n\n')


class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')

        if len(value) < self._min_length:
            raise ValueError(
                f'Value should be at least {self._min_length} characters'
            )
        if len(value) > self._max_length:
            raise ValueError(
                f"Value cannot exceed {self._min_length} characters"
            )
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]

    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.data[key]


class PersonExample1:
    __slots__ = '__weakref__',

    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)

    def __eq__(self, other):
        return (
            isinstance(other, PersonExample1) and
            self.first_name == other.first_name and
            self.last_name == other.last_name
        )


class BankAccount:
    __slots__ = '__weakref__',
    account_number = ValidString(5, 255)

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.account_number == other.account_number


# create the instance for Person
person2 = PersonExample1()
person3 = PersonExample1()

person2.first_name, person2.last_name = 'FRED', 'Baptist'
person3.first_name, person3.last_name = 'Vivek', 'reddyvari'

b1, b2 = BankAccount(), BankAccount()

b1.account_number, b2.account_number = 'Savings', 'Checking'

print(f"checking person2: {person2.first_name, person2.last_name}")
print(f"checking person3: {person3.first_name, person3.last_name}")

# checking bank accounts
print(f"checking Bank Accounts(b1, b2): {b1.account_number, b2.account_number}")

# check persons
print(PersonExample1.first_name.data, end='\n\n')
print(PersonExample1.last_name.data, end='\n\n')
print(BankAccount.account_number.data, end='\n\n')
print("Deletion of person2, person3, b1, b2")
del person2
del person3
del b1
del b2

# check references
print(f"after deletion {PersonExample1.first_name.data}", end='\n\n')

