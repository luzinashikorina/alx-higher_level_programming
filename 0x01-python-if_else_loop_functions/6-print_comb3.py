#!/usr/bin/python3
for firstDigit in range(10):
    for secondDigit in range(10):
        if firstDigit < secondDigit:
            print('{:d}{:d}'.format(firstDigit, secondDigit), end='')
            if firstDigit < 8:
                print(', ', end='')
print('\n', end='')
