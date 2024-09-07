import pytest

from practice_with_exceptions.main import Employee


def test_raises():
    emp1 = Employee('Ivan', 'Ivanov', 50000)
    with pytest.raises(TypeError) as e_info:
        emp1 + '50000'


def test_raises_with_dict():
    emp1 = Employee('Ivan', 'Ivanov', 50000)
    with pytest.raises(TypeError) as e_info:
        emp1 + {'name': 1}

