from src.toolkit.calculator import tokenize_fsm
from src.toolkit.calculator import calc
import pytest

def test_operation_priority():
    assert calc("2+3-5*-7") == 40

def test_left_to_right_priority():
    assert calc("12/2/3*4") == 8

def test_consecutive_signs():
    assert calc("5+---2") == 3

def test_floating_point():
    assert calc("2.5*4-1.5/0.5") == 7.0

def test_division_precision():
    assert calc("10/3+2") == pytest.approx(5.3333333)

def test_large_numbers():
    assert calc("100000000000*100000000000-1") == 9999999999999999999999

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        calc("5+10/0-3")

def test_spaces_handling():
    assert calc("  2   +  3 *   -5  ") == -13

def test_invalid_syntax_trailing_operator():
    with pytest.raises((ValueError)):
        calc("2+3-5*")

def test_invalid_syntax_double_binary_operators():
    with pytest.raises((ValueError)):
        calc("2+*3-5")

def test_floating_point2():
    assert calc("2.5*4-1.5/0.5") == 7.0

def test_minus_substruction():
    assert calc("-5--5") == 0

def test_alternating_signs():
    assert calc("2+-+3") == -1

def test_alternating_signs_two_minus():
    assert calc("2+--+3") == 5

def test_fractial_chain():
    assert calc("1/2/2/2") == 0.125

def test_single_negative_number():
    assert calc("-99.9") == -99.9