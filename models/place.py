#!/usr/bin/python3
"""Define Place class for Airbnb console"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Place(BaseModel, Base):
    """defines place attributes for user

    city_id(str): id of city where place is located
    user_id(str): id of user 
    name (str): name of place
    description(str): brief description of place
    number_rooms(int): number of rooms in place
    number_bathrooms(int): number of bathrooms in place
    max_guest(int): maximum number of guests place can accommodate
    price_by_night(int): unit price of place per night
    latitude(float): GPS coordinates of place
    longitude(float): GPS coordinates of place
    """
    
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
