import pytest
from ejercicio_funciones import *

@pytest.mark.parametrize("number, res",[
    (1056, 12),
    (111, 3),
    (902, 11),
])

def test_sumDigits(number, res):
    assert sumDigits(number)==res