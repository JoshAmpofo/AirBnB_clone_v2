#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base()
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import models
from models.base_model import BaseModel, Base
import shlex


class State(BaseModel):
    """Define State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        mod_args = model.storage.all()
        mod_args_list = [mod_args[key] for key in mod_args.keys() if
                         isinstance(mod_args[key], City) and
                         mod_args[key].state_id == self.id and
                         key.replace(".", " ").split[0] == 'CIty']
        return mod_args_list
