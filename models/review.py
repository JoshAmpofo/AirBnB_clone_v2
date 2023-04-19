#!/usr/bin/python3
"""Defines Review class for Airbnb clone"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """Define Reiew attributes for place/service review in Airbnb

    Attrs:
        place_id(str): id of place review is being given
        user_id(str): id of user giving review
        text(str): review message
    """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
