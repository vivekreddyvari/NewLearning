from enum import Enum, unique
from functools import total_ordering
from http import HTTPStatus


class GenericException(Exception):
    """ This class will raise an exception """
    def __new__(cls, member_value, member_phrase):
        # print(cls, member_value, member_phrase)
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member
    pass


class Timeout(Exception):
    pass


@unique
class AppExceptionTrail(Enum):
    Generic = 100, GenericException, 'Application exception'
    Timeout = 101, Timeout, 'Timeout Connecting to resource'
    NotAnInteger = 200, ValueError, 'Value must be an Integer'
    NotAlist = 201, ValueError, 'Value must be a list'

    def __new__(cls, ex_code, ex_class, ex_message):
        # print(cls, member_value, member_phrase)
        member = object.__new__(cls)
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member


try:
    raise AppExceptionTrail.Timeout.exception(f"{AppExceptionTrail.Timeout.value} - {AppExceptionTrail.Timeout.message}")
except Exception as ex:
    print(ex)


@unique
class AppExceptionTrailOne(Enum):
    Generic = 100, GenericException, 'Application exception'
    Timeout = 101, Timeout, 'Timeout Connecting to resource'
    NotAnInteger = 200, ValueError, 'Value must be an Integer'
    NotAlist = 201, ValueError, 'Value must be a list'

    def __new__(cls, ex_code, ex_class, ex_message):
        # print(cls, member_value, member_phrase)
        member = object.__new__(cls)
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

    @property
    def code(self):
        return self.value

    def throw(self):
        raise self.exception(f"{self.code} - {self.message}")

try:
    AppExceptionTrailOne.NotAnInteger.throw()
except Exception as ex:
    print(ex)


@unique
class AppException(Enum):
    Generic = 100, GenericException, 'Application exception'
    Timeout = 101, Timeout, 'Timeout Connecting to resource'
    NotAnInteger = 200, ValueError, 'Value must be an Integer'
    NotAlist = 201, ValueError, 'Value must be a list'

    def __new__(cls, ex_code, ex_class, ex_message):
        # print(cls, member_value, member_phrase)
        member = object.__new__(cls)
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

    @property
    def code(self):
        return self.value

    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f"{self.code} - {message}")


try:
    AppException.NotAlist.throw('custom message')
except Exception as ex:
    print(ex)

print(list(AppException))

mes = [(ex.message, ex.code, ex.exception.__name__, ex.message) for ex in AppException]
print(mes)