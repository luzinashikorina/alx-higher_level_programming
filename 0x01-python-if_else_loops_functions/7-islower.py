#!/usr/bin/python3
def islower(c):
    asciiValue = ord(c)
    for i in range(97, 123):
        if asciiValue == i:
            return True
        else:
            return False
