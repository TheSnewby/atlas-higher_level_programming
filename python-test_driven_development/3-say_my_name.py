#!/usr/bin/python3
"""Say my name is you know it."""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    0) simple, successful case
    >>> say_my_name('John', 'Adams') #0
    My name is John Adams

    1) parameters must be strings
    >>> say_my_name(['John'], 'Adams') #1
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    2) parameters must be strings
    >>> say_my_name('John', ['Adams']) #2
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    3) first_name mustn't be empty
    >>> say_my_name() #3
    Traceback (most recent call last):
        ...
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
