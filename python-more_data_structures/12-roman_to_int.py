#!/usr/bin/python3
def roman_to_int(roman_string):
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000}
    if not isinstance(roman_string, str) or roman_string == '':
        return 0
    roman_list = list(roman_string)
    sum = 0

    if len(roman_list) == 1:
        return numerals[roman_list[0]]
    sum = 0
    for i in range(len(roman_list)):
        if i == len(roman_list) - 1:
            sum += numerals[roman_list[i]]
        elif numerals[roman_list[i]] < numerals[roman_list[i + 1]]:
            sum -= numerals[roman_list[i]]
        else:
            sum += numerals[roman_list[i]]
    return sum
