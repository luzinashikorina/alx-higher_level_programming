#!/usr/bin/python3
"""
Module 2
Defines class Square with private attribute size
"""


class Square:
    """
    Class Square definition

    Args:
        size (int): length of side of square
    """
    def __init__(self, size=0):
        """
        Initializes the data

        Attributes:
            size: has to be int
        """
        if int(size) != size:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
