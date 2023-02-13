#!/usr/bin/python3
"""
Contains 'Square' class definiton
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inherits inherits from 'Rectangle' class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            size (int): size of the square
            x (int): x axis of the square
            y (int): y axis of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """Returns string representation of the instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the value of 'size'
        Returns:
            value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of 'width'"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the class"""
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                    self.height = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        elif kwargs:
            for kwarg in kwargs:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.width = kwargs["size"]
                    self.height = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}


