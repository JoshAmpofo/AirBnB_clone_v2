#!/usr/bin/python3
"""Initialize both file storage systems"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os


env = getenv('HBNB_TYPE_STORAGE')

if env == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
