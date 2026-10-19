import pytest
from src.toolkit.converter import convert

# Тесты для группы "длина"
def test_length_same_units():
    assert convert(10.0, "mm", "mm") == 10.0

def test_length_mm_to_cm():
    assert convert(50.0, "mm", "cm") == 5.0

def test_length_m_to_km():
    assert convert(1500.0, "m", "km") == 1.5

def test_length_case_insensitivity():
    assert convert(2.0, "KM", "m") == 2000.0

# Тесты для группы "масса"
def test_mass_g_to_kg():
    assert convert(2500.0, "g", "kg") == 2.5

def test_mass_kg_to_g():
    assert convert(1.23, "kg", "g") == 1230.0

def test_mass_case_insensitivity():
    assert convert(5.0, "Kg", "G") == 5000.0

# Тесты для группы "температура"
def test_temp_c_to_f():
    assert convert(0.0, "c", "f") == 32.0

def test_temp_c_to_k():
    assert convert(27.0, "c", "k") == 300.15

def test_temp_k_to_c():
    assert convert(0.0, "k", "c") == -273.15

def test_temp_case_insensitivity():
    assert convert(100.0, "C", "f") == 212.0

# Тесты на ограничения и ошибки
def test_error_cross_group_conversion():
    with pytest.raises(ValueError):
        convert(10.0, "m", "kg")

def test_error_below_absolute_zero_c():
    with pytest.raises(ValueError):
        convert(-274.0, "c", "k")

def test_error_below_absolute_zero_k():
    with pytest.raises(ValueError):
        convert(-1.0, "k", "c")

def test_error_unknown_units():
    with pytest.raises(ValueError):
        convert(10.0, "abc", "m")
