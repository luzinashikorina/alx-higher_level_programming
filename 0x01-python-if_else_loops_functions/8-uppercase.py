#!/usr/bin/python3
def uppercase(iString):

    for i in iString:
        if 97 <= ord(i) <= 122:
            i = chr(ord(i) - 32)
        print('{:s}'.format(i), end='')

    print('\n', end='')
