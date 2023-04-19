#!/usr/bin/python3
"""This module defines a class User using db_storage as engine"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """Defines User class with the following attributes

    email(str): user login email
    password(str): user login password
    first_name(str): first name of user
    last_name(str): last name of user
    """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='user')
