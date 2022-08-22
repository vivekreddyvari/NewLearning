

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

    


