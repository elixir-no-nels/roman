import pytest

from roman import __version__
from roman.conversions import calc_next_smaller_decimal_base
from roman.conversions import decimal_to_roman


def test_version():
    assert __version__ == '0.1.0'


def test_simple_numbers():
    assert decimal_to_roman(1) == 'I'
    assert decimal_to_roman(2) == 'II'
    assert decimal_to_roman(3) == 'III'
    assert decimal_to_roman(5) == 'V'
    assert decimal_to_roman(6) == 'VI'
    assert decimal_to_roman(7) == 'VII'
    assert decimal_to_roman(8) == 'VIII'
    assert decimal_to_roman(10) == 'X'
    assert decimal_to_roman(11) == 'XI'
    assert decimal_to_roman(12) == 'XII'
    assert decimal_to_roman(13) == 'XIII'
    assert decimal_to_roman(15) == 'XV'
    assert decimal_to_roman(16) == 'XVI'
    assert decimal_to_roman(17) == 'XVII'
    assert decimal_to_roman(18) == 'XVIII'


def test_complex_numbers():
    assert decimal_to_roman(4) == 'IV'
    assert decimal_to_roman(9) == 'IX'
    assert decimal_to_roman(14) == 'XIV'
    assert decimal_to_roman(19) == 'XIX'
    assert decimal_to_roman(29) == 'XXIX'
    assert decimal_to_roman(39) == 'XXXIX'
    assert decimal_to_roman(49) == 'XLIX'
    assert decimal_to_roman(84) == 'LXXXIV'
    assert decimal_to_roman(99) == 'XCIX'
    assert decimal_to_roman(1498) == 'MCDXCVIII'
    assert decimal_to_roman(1989) == 'MCMLXXXIX'


def test_calc_next_smaller_decimal_base():
    with pytest.raises(ValueError):
        calc_next_smaller_decimal_base(1)

    assert calc_next_smaller_decimal_base(2) == 1
    assert calc_next_smaller_decimal_base(9) == 1
    assert calc_next_smaller_decimal_base(10) == 1

    assert calc_next_smaller_decimal_base(11) == 10
    assert calc_next_smaller_decimal_base(50) == 10
    assert calc_next_smaller_decimal_base(99) == 10
    assert calc_next_smaller_decimal_base(100) == 10

    assert calc_next_smaller_decimal_base(101) == 100
    assert calc_next_smaller_decimal_base(1000) == 100

    assert calc_next_smaller_decimal_base(1001) == 1000
    assert calc_next_smaller_decimal_base(9999) == 1000
