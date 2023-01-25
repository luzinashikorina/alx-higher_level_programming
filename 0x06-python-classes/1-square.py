#!/usr/bin/python3
"""
Module 1
Defines class Square with private attribute size
"""


class Square:
    """
    Class Square definition

    Args:
        size (int): length of side of square
    """
    def __init__(self, size):
        """
        Initializes the data

        Attributes:
            size: size
        """
        self.__size = size
