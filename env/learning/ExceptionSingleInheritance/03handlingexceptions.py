import json

""" 
Handling Exceptions using try:

try:
    code that we want to protect from some potential exceptions.
 keep this guarded code as short as possible
 often just a single statment
except:
    code that will run if that specified <ExceptionType> occurs (or any subclass)


    
finally:
    code that always executes - whether exception occured or not
    
else: 
    coee that executes if try terminates normally
    (an except clause must be present)
    

"""
try:
    import sys
except ImportError as ex:
    print(ex)
    # Order matter
finally:
    # appears 0 or 1 times
    print('success')
    print(f" This is python software {sys.version} version")
    print(f" This is the OS-VERSION {sys.platform}")
    for num, mod in enumerate(dir(sys)):
        print(f"Number {num} = Module `{mod}`")
    print(f"Version Information {sys.version_info}")
    print(f"{print(dir(sys.version_info))}")
    version_major = sys.version_info.major
    version_minor = sys.version_info.minor
    version_micro = sys.version_info.micro
    version_releaselevel = sys.version_info.releaselevel

    if version_major == 3 and version_minor >= 10:
        print(f"{version_major}.{version_minor}.{version_micro}")


# else:
    # print('something went wrong')
    # appears 0 or 1 times # only allowed if an except clause is present


lis = [ 1, 2, 3]
try:
    lis[3]
except IndexError:
    print(f'{IndexError} - invalid Index')
except LookupError:
    print(f"{LookupError} - Lookup Error")

# Try and finally - mostly used in scenario
# like open the file in try block and close the file in finally block

try:
    with open('example.txt' 'r') as file:
        data = file.read()
except FileNotFoundError:
    print('File Not Found')
# finally:
    # file.close()

# if exception handler raises an exception>
"""
Everything works as normal - If the exception is not handled, it is propageted up.
EAFP in python
Easier to ask for Permission

# pythonic way:
try:
    with open('file_name', 'r') as f:
except OSerror:
    print('error')
finally:
    f.close()

other way:
if os.path.exists(fname) and not os.path.isdir(fname):
    f = open(fname, 'r')
    f.close()
    

"""

from os import path
if path.exists('example.txt') and not path.isdir('example.txt'):
    f = open('example.txt', 'r')
    data_info = f.read()
    print(data_info)
    f.close()

# Coding
try:
    raise ValueError('Custom Message')
except ValueError as ex:
    print(ex)


def func_1():
    raise ValueError('bad value')

try:
    func_1()
except ValueError as ex:
    print('Handling a value error', repr(ex))
except IndexError as ex:
    print('Handling an index error', repr(ex))

    
try:
    raise TypeError('error')
except ValueError as ex:
    print('handling value exception ', repr(ex))
except Exception as ex:
    print('handling exception ', repr(ex))


# Finally Block
"""
Always run after code finish running in what ever the case it is...
"""

try:
    raise ValueError()
except ValueError:
    print('handle error')
finally:
    print('running finally')

"""
try:
    a.append[0]
except ValueError or IndexError or NameError:
    print('value error')
else:
    print('no exception')
"""

json_data = """{"Alex": {"age": 18}, "Bryan" : {"age": 21, "city": "London"}, "Guido" : {"age": "unknown"}}"""
data = json.loads(json_data)

print(data)


class Person:
    __slots__ = 'name', '_age'

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError('Invalid age')

    def __repr__(self):
        return f"Person((name={self.name}, age={self.age}))"

persons = []

for name, attributes in data.items():
    try:
        p = Person(name)
        for attrib_name, attrib_value in attributes.items():
            try:
                setattr(p, attrib_name, attrib_value)
            except AttributeError:
                print(f"Ignoring Attribute: {name}.{attrib_name}={attrib_value}")
    except ValueError as ex:
        print(f"Data for Person({name}) contains an invalid attribute value: {ex}")
    else:
        persons.append(p)


print(persons)
print('ENd')
print('\n\n\n')


# distinct helper function
# string to int - conversion
def convert_int(val):
    if not isinstance(val, int):
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError('Integer Values 0 or 1 only')
    return bool(val)


def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
    # casefold for case sensitive
    val = val.casefold()
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False, 0, 1, ...')


class ConversionError(Exception):
    pass


def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type is inadmissible...')


    except ValueError as ex:
        raise ConversionError(f'the value {val} converted to a bool: {ex}')
    else:
        return b


values = [True, 0, 'T', 'False', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)

    except ConversionError as ex:
        result = str(ex)

    print(f" {value} = {result}")

print('\n\n\n\n')


def make_bool_ver_1(val):
    if isinstance(val, int):
        if val in {0, 1}:
            return bool(val)
        else:
           raise ConversionError("Invalid Integer Value")

    if isinstance(val, str):
        if val.casefold() in {'1', 'true', 't'}:
            return True
        if val.casefold() in {'0', 'false', 'f'}:
            return False
        raise ConversionError('Invalid String Value')
    raise ConversionError('Invalid Type')

values = [True, 0, 'T', 'False', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool_ver_1(value)

    except ConversionError as ex:
        result = str(ex)

    print(f" {value} = {result}")


def get_item_forgive_me(seq, idx, default=None):
    try:
        return seq[idx]
    except (IndexError, TypeError, KeyError):
        return default


def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        if isinstance(seq, dict):
            return seq.get(idx, default)
        elif isinstance(idx, int):
            if idx < len(seq):
                return seq[idx]

    return default


print(get_item_forgive_me([1,2,3], 10, 'Nope'))
print(get_item_ask_perm([1,2,3], 10, 'Nope'))

print(get_item_forgive_me({'a': 100}, 'a'))

print(get_item_ask_perm({'a': 100}, 'a'))


class ConstantSequence:
    def __init__(self, val):
        self.val = val
    def __getitem__(self, idx):
        return self.val

seq = ConstantSequence(10)
print(seq[0], seq[1])

get_item_forgive_me(seq, 10, 'Nope')
# get_item_ask_perm(seq, 10, 'Nope')


print(get_item_forgive_me([1,2,3,4], slice(1,3)))
