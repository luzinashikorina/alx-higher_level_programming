#!/usr/bin/python3
"""Contains a Class 'Base'"""
import json


class Base:
    """
        Defines the class 'Base'

        Attributes:
            id (int): instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes class and object data

            Args:
                id (int): integer passed on object creation
        """
        if not id is None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string represntation
            of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Returns JSON string representation
            of list_objs
        """
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(objs))
