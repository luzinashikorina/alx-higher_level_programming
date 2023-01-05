#!/usr/bin/python4
unwantedLetters = [101, 113]

for i in range(97, 123):
    if i in unwantedLetters:
        continue
    print('{:c}'.format(i), end='')
