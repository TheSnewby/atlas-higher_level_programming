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
            if text[i] not in ['?', ':', '.']:
                if i == len(text) - 1:
                    new_string += text[i]
                    print(new_string.strip(), end='')
                else:
                    new_string += text[i]
            else:
                new_string += text[i]
                print(new_string.strip())
                print()
                new_string = ''
# text_indentation('Holberton School')
# print('--')
# text_indentation('Holberton.School')
# print('--')
#text_indentation('Holberton. School? How are you: John')