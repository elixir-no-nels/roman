import math

DECIMAL_TO_ROMAN_LETTER = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def decimal_to_roman(decimal: int) -> str:
    roman = ''
    remainder = decimal

    for roman_base in DECIMAL_TO_ROMAN_LETTER.keys():
        while remainder >= roman_base:
            roman, remainder = append_letter(roman, remainder, roman_base, subtract)

        if roman_base > 1:
            next_decimal_base = calc_next_decimal_base(roman_base)
            if remainder >= roman_base - next_decimal_base:
                roman, remainder = append_letter(roman, remainder, next_decimal_base, add)
                roman, remainder = append_letter(roman, remainder, roman_base, subtract)

    return roman


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def calc_next_decimal_base(roman_base):
    return 10**math.floor(math.log10(roman_base - 1))


def append_letter(roman, remainder, roman_letter_decimal, remainder_operation):
    roman += DECIMAL_TO_ROMAN_LETTER[roman_letter_decimal]
    remainder = remainder_operation(remainder, roman_letter_decimal)

    return roman, remainder
