import logging
from logging import Logger

# Raising Exceptions
""""
Raising an Exception:
    -> Use the raise statement
    -> Raised object must be an instance of BaseException.
    -> __init__ can handle *args
        -> accessible via args attribute of exception object (instance)
        -> used for str() and repr() representations
        -> subclasses inherit this behaviour
    
Re-Raising current exception being handled.
When we are handling an exception:
-> inside an except block
-> we can re-raise the current excepting using raise
-> this will resume exception propagation.

Exception Trace track:
    -> We have seen: exception handlers that themselves raise exceptions (nested exceptions)
    -> final exception traceback shows us a history of this.

try:
    raise ValueError()
except ValueError:
    try:
        raise TypeError()
    except TypeError()
        raise KeyError()

other ways can be from
try:
    raise ValueError()
except ValueError:
    try:
        raise TypeError()
    except TypeError()
        raise KeyError() from None.
        
"""

# Coding

# checking the directory of Logging
for num, mod in enumerate(dir(logging.Logger)):
    print(f"{num}={mod}")


class Person:
    pass


ex = BaseException('a', 'b')
print(f"{str(ex), repr(ex)}, {ex.args}")

try:
    raise ValueError('some message', 100, 200)
except ValueError as ex:
    print(ex.args)


def div(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging exception', repr(ex))
        raise


try:
    div(1, 0)
except ZeroDivisionError as ex:
    print(ex)


class CustomError(Exception):
    """ a custome exception"""


def my_func(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging exception', repr(ex))
        raise CustomError("ex.args")


try:
    my_func(1, 0)
except CustomError as ex:
    print(repr(ex))


def convert_int(val):
    if not isinstance(val, int):
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError('Integer Values 0 or 1 only')
    return bool(val)


class ConversionError(Exception):
    pass


def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()

    # case fold for case-sensitive
    val = val.casefold()
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False, 0, 1, ...')


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
        raise ConversionError(f'the value {val} converted to a bool: {ex}') from None
    else:
        return b


# make_bool('ABC')
""" 
try:
    raise ValueError('level 1')
except ValueError as ex:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('Value Error occurred') from None
"""

"""
try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('cannot recover') from ex_1

"""

