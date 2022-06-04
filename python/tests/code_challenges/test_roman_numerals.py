import pytest
from code_challenges.roman_numerals import roman_to_arabic, convert_character

def test_exists():
    assert roman_to_arabic
    assert convert_character

def test_roman_to_arabic():
    num = roman_to_arabic('XI')
    assert num == 11

def test_convert_characters():
    m = convert_character('M')
    D = convert_character('D')
    C = convert_character('C')
    L = convert_character('L')
    X = convert_character('X')
    V = convert_character('V')
    I = convert_character('I')
    assert m == 1000
    assert D == 500
    assert C == 100
    assert L == 50
    assert X == 10
    assert V == 5
    assert I == 1
