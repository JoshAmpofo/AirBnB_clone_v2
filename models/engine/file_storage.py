#!/usr/bin/python3
"""This module defines a class to manage file storage for AirBnB clone"""
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of Airbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns list of objects of one type of class"""
        dic_t = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                separator = key.replace('.', ' ')
                separator = shlex.split(separator)
                if (separator[0] == cls.__name__):
                    dic_t[key] = self.__objects[key]
            return (dic_t)
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                for key, val in (json.load(f)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes obj from __objects if obj exists
        If obj is None, method does nothing
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """reload objects"""
        self.reload()
