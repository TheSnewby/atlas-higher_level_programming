#!/usr/bin/python3
"""Text indentation is text indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ?, and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        new_string=''
        for i in range(len(text)):
            if text[i] != '!' and text[i] != ':' and text[i] != '.':
                if i == len(text) - 1:
                    new_string += text[i]
                    print(new_string.strip())
                else:
                    new_string += text[i]
            else:
                new_string += text[i]
                print(new_string.strip())
                print()
                new_string = ''
