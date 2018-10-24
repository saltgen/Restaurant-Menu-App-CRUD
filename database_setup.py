#!/usr/bin/env python

import sys  # no of funcs and modules, useful to manipulate Python environment

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine

# IMPORTS FOR CONFIG AND CLASS CODE
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship  # for mapper

from sqlalchemy import create_engine


# LETTING ORM KNOW TABLES ARE SQLA CLASSES THAT CORRESPOND TO DATABASE TABLES
Base = declarative_base()

# CREATING A USER MODEL


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

# CREATING THE RESTAURANT MODEL


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # SERIALIZING FORMAT FOR RESTAURANT MODEL DATA

    @property
    def serialize(self):
        # Return object data in easily serializeable format
        return {
            'name': self.name,
            'id': self.id,
        }

# CREATING THE MENU ITEM MODEL


class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    # ESTABLISHING A FOREIGN KEY RELATIONSHIP
    restaurant = relationship(Restaurant)

    # SERIALIZING FORMAT FOR RETAURANT MODEL DATA

    @property
    def serialize(self):
        # RETURNS OBJECT DATA IN EASY TO READ SERIALIZED FORMAT
        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


# CREATING DATABASE FILE
engine = create_engine('sqlite:///restaurantmenuwithusers.db')

# ADDS THE ABOVE/CREATED CLASSES TO DATABASE
Base.metadata.create_all(engine)
