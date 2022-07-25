"""
Test the validators functions
command line: python -m pytest tests/test_validators.py
"""

import pytest
from OOP.Project3.app.utils.validators import validate_integer


class TestIntegerValidator:
    def test_valid(self):
        validate_integer('arg', 10, 0, 20, 'Custom Min Message', 'Custom max message')

    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer('arg', 1.5)

    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 100)
        assert 'arg' in str(ex.value)
        assert '100' in str(ex.value)

    def test_min_custom_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 100, custom_min_message='custom min')
        assert str(ex.value) == 'custom min'

    def test_max_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 1, 5)
        assert 'arg' in str(ex.value)
        assert '5' in str(ex.value)

    def test_max_custom_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 10, 1, 5, custom_max_message='custom max')
        assert str(ex.value) == 'custom max'
