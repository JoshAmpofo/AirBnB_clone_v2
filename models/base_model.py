#!/usr/bin/python3
"""This module defines a base class for all models in our Airbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all Airbnb models"""
    id = Column(String(60), unique=True, primary_key=True, nullabale=False)
    created_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)
    update_at = Column(DateTime, default=(datetime.utcnow()), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model

        Args:
            *args: unpacks arguments as is
            **kwargs(dict): unpacks args in a key/value format
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(val,
                                              '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, val)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.create_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """returns str canonical representation of instances"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format and returns __dict__ value"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Deletes current instance fro storage"""
        models.storage.delete(self)
