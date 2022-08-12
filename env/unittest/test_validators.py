import pytest
from OOP.Descriptors.env.learning.Project.validators import CharField, IntegerField


class Person:
    age = IntegerField(1, 99)
    first_name = CharField(2, 20)
    last_name = CharField(4, 10)


class TestIntegerValidator:

    def test_length_integer_field(self):

        # change number of age min
        p = Person()
        p.age = 1
        assert(p.age > -1)

        try:
            p.age = 100
        except ValueError as ex:
            print(ex)

        try:
            p.age = 0
        except ValueError as ex:
            print(ex)

    def test_integer_type(self):
        p = Person()
        try:
            p.age = 'abc'
        except ValueError as ex:
            print(ex)


class TestCharValidator:
    def test_length_char_field(self):
        p = Person()

        # min
        try:
            p.first_name = 'a'
        except ValueError as ex:
            print(ex)

        # max
        try:
            p.first_name = 'abcedfghihjklmnopqurstev'
        except ValueError as ex:
            print(ex)

        pass

    def test_length_char_type(self):
        p = Person()
        try:
            p.first_name = 123
        except ValueError as ex:
            print(ex)

        pass


