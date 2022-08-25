from logging import Logger
import sys
from http import HTTPStatus
import json
from datetime import datetime


# Creating Custom Exceptions
message = 'custom exception'
message_title = message.title()
print(message_title.center(100))

"""
Creating New Exception Classes
    -> Create a new class that inherits from Exception (or one of its subclasses)
        -> recall BaseException is the base class for all exceptions.
            BaseException
                Exception
                
                SystemExit
                KeyBoardInterrupt
                GeneratorExit
                

"""


# Creating New Exception class
class WidgetException(Exception):
    """ base custom exception for widget Library """
    pass


# ValueError class for Widgets
class WidgetValueError(ValueError):
    """ custom exception ValueError """
    pass


class OutofStockException(WidgetException):
    """ Out of stock Exception """
    pass

# creating Hierarchy of Custom Exceptions:
"""
    -> Often we have an entire set of custom exceptions
    -> keep the exceptions organized -> just like python
    -> create a hierarchy of custom exceptions -> allows trapping exceptions at multiple levels
    
"""


class ExampleExceptionOne(Exception):
    # now we can use above class and can be inherited to the sub other class
    class ExampleStockExceptionOne(WidgetException):
        pass

    # Now another class inherit above exception too
    class OutOfStock(WidgetValueError):
        pass

    pass


# Extending Functionality
"""
exceptions are classes:
    -> Add functionality (properties, methods, attributes)
    -> Even implement special methods (__str__, __repr__, etc)
    -> for example, add auto-logging to your exemptions.
    -> use for consistent output mechanisms (e.g. json representation of the exceptions)

Multiple Inheritance
    exceptions like any class can inherit from multiple classes
    keeping it simple
    -> custom exceptions can inherit multiple exceptions.
    
    
    class WidgetException(Exception)
        class SalesException(WidgetException)
            class InvalidSalePrice(SalesException, ValueError)
            
if an InvalidSalePrice Exception is raised
    -> can be trapped with either InvalidSalePrice or ValueError
    
    
"""


# Coding:
class TimeOutError(Exception):
    """ Timeout Exception """
    pass

try:
    raise TimeOutError("Timeout Occurred")
except Exception as ex:
    print(ex.args, ex.__traceback__)


class ReadOnlyError(AttributeError):
    """ Indicates an attribute is read-only """

# Exception catch exact error
try:
    raise ReadOnlyError('Account number is read-only', 'BA10001')
except ReadOnlyError as ex:
    print(repr(ex))

# Exception catch at BaseException Level.
try:
    raise ReadOnlyError('Account number is read-only', 'BA10001')
except BaseException as ex:
    print(repr(ex))


# Webscrapper - product information and prices
class WebScrapperException(Exception):
    """ Base Exception for Webscrapper """


class HTTPException(WebScrapperException):
    """ General HTTP exception for Webscrapper """


class InvalidUrlException(HTTPException):
    """ Indicates the  url is invalid (dns lookup fail) """


class TimeOutException(HTTPException):
    """Indicates a general timeout exception in http Connectivity """


class PingTimeoutException(TimeOutException):
    """ Ping time out """


class LoadTimeoutException(TimeOutException):
    """Page load timeout """


class ParserException(WebScrapperException):
    """ General page parsing exception """


try:
    raise PingTimeoutException('Ping to www..... timeout')
except HTTPException as ex:
    print(repr(ex))


# PingTimeoutException('Ping to www.... timeout')
# DB and Web exceptions
class APIException(Exception):
    """Base APi Exception."""


class ApplicationException(APIException):
    """ Indicates an application error (not user caused) - 5xx HTTP type Error """


class DBException(ApplicationException):
    """ General database Exception """


class DBConnectionError(DBException):
    """ Indicates an error connecting to database """


class ClientException(APIException):
    """ Indicates exception that was caused by user, not an internal error """


class NotFoundError(ClientException):
    """ Indicates resource was not Found """


class NotAuthorizedError(ClientException):
    """ User is not authorized to perform request action on resource """


class Account:
    """ Account details"""
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type


def lookup_account_by_id(account_id):
    """ check the account """
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f"Account number {account_id} is invalid ")

    if account_id < 100:
        raise DBConnectionError(f"Permanent failure connecting to Database")
    elif account_id < 200:
        raise NotAuthorizedError(f"User does not have permission to read this account")
    elif account_id < 300:
        raise NotFoundError(f"Account not found")
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except ApplicationException as ex:
        return HTTPStatus.INTERNAL_SERVER_ERROR, str(ex)
    except NotFoundError as ex:
        return HTTPStatus.NOT_FOUND, 'The account {} does not exist'.format(account_id)
    except NotAuthorizedError as ex:
        return HTTPStatus.UNAUTHORIZED, 'You do not have the proper authorization...'
    except ClientException as ex:
        return HTTPStatus.BAD_REQUEST, str(ex)
    else:
        return HTTPStatus.OK, {'id': account.account_id, "type": account.account_type}

print(get_account('abc'))
print(get_account(50))
print(get_account(150))
print(get_account(250))
print(get_account(350))


class APIException(Exception):
    """Base APi Exception."""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred'
    user_err_msg = "We are sorry! Unexcepted error occurred on our end "

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg


try:
    raise APIException('Custom message....', 10, 20, user_err_msg='custom user message')
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)


# With Json exception handling
class APIException(Exception):
    """Base APi Exception."""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred'
    user_err_msg = "We are sorry! Unexcepted error occurred on our end "

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

try:
    raise APIException()
except APIException as ex:
    print(repr(ex))
    print(ex.to_json())


# with date and time exception
class APIExceptionFinal(Exception):
    """Base APi Exception."""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred'
    user_err_msg = "We are sorry! Unexcepted error occurred on our end "

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f"Exception: {datetime.utcnow().isoformat}: {exception}")


try:
    raise APIExceptionFinal()
except APIExceptionFinal as ex:
    ex.log_exception()
    print(ex.to_json())


# Default Messages:
class ApplicationExceptionFinal(APIExceptionFinal):
    """ Indicates an application error (not user caused) - 5xx HTTP type Error """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Generic server side exception'
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class DBExceptionFinal(ApplicationExceptionFinal):
    """ General database Exception """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database Exception '
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class DBConnectionErrorFinal(DBExceptionFinal):
    """ Indicates an error connecting to database """
    https_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'Database Connection Exception '
    user_err_msg = 'We are sorry, An unexcepted error occurred on our end'


class ClientExceptionFinal(APIExceptionFinal):
    """ Indicates exception that was caused by user, not an internal error """
    https_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = 'Client submitted bad request '
    user_err_msg = 'A bad request was received'


class NotFoundErrorFinal(ClientExceptionFinal):
    """ Indicates resource was not Found """
    https_status = HTTPStatus.NOT_FOUND
    internal_err_msg = 'Resource Not Found '
    user_err_msg = 'Requested resource was not found '


class NotAuthorizedErrorFinal(ClientExceptionFinal):
    """ User is not authorized to perform request action on resource """
    https_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = 'Client not authorized to perform operation '
    user_err_msg = 'You are not authorized to perform this request '


def lookup_account_by_id_final(account_id):
    """ check the account """
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientExceptionFinal(f"Account number {account_id} is invalid ",
                              f"account_id={account_id}, ",
                              f"type error - account number not an integer")

    if account_id < 100:
        raise DBConnectionErrorFinal(f"Permanent failure connecting to Database, "
                                f"db=db01")
    elif account_id < 200:
        raise NotAuthorizedErrorFinal(f"User does not have permission to read this account"
                                 f"account_id = {account_id}")
    elif account_id < 300:
        raise NotFoundErrorFinal(f"Account not found",
                            f" account_id = {account_id}")
    else:
        return Account(account_id, 'Savings')


def get_account(account_id):
    try:
        account = lookup_account_by_id_final(account_id)
    except APIExceptionFinal as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {'id': account.account_id, "type": account.account_type}


get_account('50')
get_account('abc')
get_account('150')
get_account('250')

get_account('350')


# Negative Integer Error
class AppException(Exception):
    """generic application exception """


class NegativeIntegerError(AppException, ValueError):
    """ Used to indicate an error when an integer is negative """


def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')


try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))


try:
    set_age(-20)
except ValueError as ex:
    print(repr(ex))