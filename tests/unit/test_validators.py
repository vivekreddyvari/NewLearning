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
