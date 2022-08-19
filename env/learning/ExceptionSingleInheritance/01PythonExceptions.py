# Imports

# Exceptions

"""
    What are Exceptions?
        -> Exceptions are objects -> they are instances of some class
        -> When an exception is raised
            -> Trigger a special execution propagation workflow
                -> Exception Handling
                -> If current call does not handle exception it is propagated up to caller
                -> call stack trace is maintained

    call function_1 (Now the call stack function_1)
        call function_2 from function_1 (Now the call stack function_2)
            call function_3 from function_2 (Now the call stack function_3)


    -> Stack trace will contain information describing the

Exception Handling:

    exceptions are not necessarily fatal i.e. do not necessarily result in program terminations

    -> We can handle exceptions as they occur
        -> do something and let program continue running 'normally'
        -> do something and elt original excepting propagate
        -> do something and raise a different exception

        -> try (compound statement)
            except
            finally
            else

What are exceptions used for?
    -> exceptions are not necessarily errors
    -> indicate some sort of anomalous behaviour
    -> sometimes not even that:
        -> consider StopIteration Exception raised by Iterator
        -> after all we would expect this to happen -> not really anomalous

Two main categories of exceptions:
    1. Compilation Exceptions (e.g. Syntax Errors)
    2. Execution Exceptions (ValueError, KeyError, StopIterations)

    Python's built in exception use inheritance to form a class Hierachy
    base exception for every exception in Python.
        -> BaseException
        -> but do not inherit from this one.

BaseException
    SystemExit (raised on sys.exit())
    KeyBoardInterrupt (Ctrl-C for example)
    GeneratorExit (raised when generator or coroutine is closed)
    Exception -> Everything else (ValueError, KeyErrors etc.)

Most of the time any exception we work with inherits from Exception.
    Direct subclasses of Exception Include:
        -> ArithmeticError
                -> FloatingPointError
                -> ZeroDivisionError
        -> AttributeError
        -> LookupError
                -> IndexError
                -> KeyError
        -> SyntaxError
        -> RuntimeError
        -> TypeError
        -> ValueError

Python Exception Hierarchy:
    When exceptions inherit from other exceptions:
        Exception > LookupError > IndexError

    an IndexError exception IS-A LookupError exception

Basic Exception Handling:
    the try Statement is used to for exception handling
 -> Multi-part statement
    -> Basic:
            try:
                code
            except ValueError as ex:
                display the code to user.

    -> Get a handle to exception object is except clause:
            try:
                code
            except ValueError as ex:
                print(ex)

"""

# coding

print(f"Handling Exceptions")
print(f"{type(BaseException), type(Exception)}")

ex = Exception()
print(f"{ex.__class__}")
print(f"{type(ex)}", end= "\n\n")

# Check the instance ex whether it belongs to Exception-Object
print(f"{isinstance(ex, Exception)}", end="\n\n")
print(f"{isinstance(ex, BaseException)}", end="\n\n")


# List
l = [1,2,3]
# print(f"{l[4]}")

# handling a error - Structure
try:
    print(f"{l[4]}")
except IndexError as ex:
    print(f"{ex.__class__}, ':', {str(ex)}, I am basic structure")

# subclass of Exception - LookupError
try:
    print(f"{l[4]}")
except LookupError as ex:
    print(f"{ex.__class__}, ':', {str(ex)}, I am Subclassed in LookUpError->IndexError")

# broad Range or Lazy way of capturing
try:
    print(f"{l[4]}")
except Exception as ex:
    print(f"{ex.__class__}, ':', {str(ex)}, I am the laziest way ")

# Custom Error Message
try:
    print(f"{l[4]}")
except:
    print('Error Occurred')

# Custom Message
ex = ValueError('Custom MESSAGE...')
print(f"{hasattr(BaseException, '__repr__'), hasattr(BaseException, '__str__')}", end="\n\n")
print(f"{str(ex), repr(ex)}", end="\n\n")


# Stack Trace:

def func_1():
    func_2()


def func_2():
    func_3()


def func_3():
    ex = ValueError('Some Custom Message')
    raise ex

# func_1()

try:
    func_1()
except ValueError as ex:
    print(ex)


def func_4():
    func_5()


def func_5():
    try:
        func_6()
    except ValueError:
        print("Error Occurred")


def func_6():
    ex = ValueError('Some Custom Message')
    raise ex

func_4()

"""
def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        yield square(seq, i)

# capture the error
l = [1,2,3]
print(list(squares(l, 3)))

"""

# Broad Range
def squareOne(seq, index):
    return seq[index] ** 2


def squaresOne(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except Exception:
            return

# capture the error
l = [1,2,3]
print(list(squaresOne(l, 4)))


# Exact error
def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except IndexError as ex:
            print(f"{ex.__class__}, ':', {str(ex)}")

# capture the error
l = [1,2,3]
print(list(squares(l, 4)))

# case 2
l = [1, 2, 3, 'a', 4]
print(list(squares(l, 10)))