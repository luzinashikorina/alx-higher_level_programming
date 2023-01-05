#!/usr/bin/python3
def print_last_digit(iNumber):
    stringFormat = repr(iNumber)
    lastCharacter = stringFormat[-1]
    lastDigit = int(lastCharacter)
    print('{:d}'.format(lastDigit), end='')
    return lastDigit
