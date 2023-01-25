#!/usr/bin/python3
"""
Module 5 
Defines class Square with a printing method
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
    def my_print(self):
        '''
        Prints the square in #s
        '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range (self.__size):
                    print("#", end = "")
                print()
        
