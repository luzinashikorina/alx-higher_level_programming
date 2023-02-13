#!/usr/bin/python3
"""Contains class 'Rectangle definiton"""
from models.base import Base


class Rectangle(Base):
    """Derives the class that inherits from 'Base' class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be >0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Retrieves the value of 'width'
        Returns:
            value of width
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the value of 'height'
        Returns:
            value of height
        """
        return self.__height
    
    @property
    def x(self):
        """Retrieves the value of 'x'
        Returns:
            value of x
        """
        return self.__x
    
    @property
    def y(self):
        """Retrieves the value of 'y'
        Returns:
            value of y
        """
        return self.__y
    
    @width.setter
    def width(self, value):
        """sets the value of 'width'"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of 'height'"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of 'x'"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value of 'y'"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of 'Rectangle' instance
        Returns:
            Calculated area of a Rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the
        charachter '#'
        """
        for i in range(self.__y):
            print()
        for col in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """Returns string representation of the instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
                i += 1
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
            if "x" in kwargs:
                self.__x = kwargs["x"]

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Rectangle"""
        return {"id": self.id, "x": self.__x, "y": self.__y, "width": self.__width, "height": self.__height}
