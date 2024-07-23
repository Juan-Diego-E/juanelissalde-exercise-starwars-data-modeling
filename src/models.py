import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore
from sqlalchemy import create_engine # type: ignore
from eralchemy2 import render_er # type: ignore

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(80))
    email = Column(String(30))
    password = Column(String(20))
    subscription_date = Column(Date)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    gender = Column(String(40))
    eye = Column(String(20))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    population = Column(Integer)
    eye = Column(String(20))
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    model = Column(String(40))
    size = Column(Integer)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
