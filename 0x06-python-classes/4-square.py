#!/usr/bin/python3
"""
Module 4
Defines class Square with getter and setter methods
"""


class Square:
    '''
    class Square definition

    Args:
        size (int): size of a side
    '''
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

    def area(self):
        '''
       Calculates and returns the area of the square

       Returns: area
        '''

        return self.__size * self.__size

    @property
    def size(self):
        '''
        Gets the value __size

        Return: size

        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the value __size
        Attributes:
            value: the new value to be
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
