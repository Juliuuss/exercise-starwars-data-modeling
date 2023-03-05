import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


 #------Usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column (String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorite_character = Column(Integer, ForeignKey('characters.id'))
    favorite_ships = Column(Integer, ForeignKey('ships.id'))
    favorite_planets = Column(Integer, ForeignKey('planets.id'))
    def to_dict(self):
        return {}



class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column (String(250), nullable=False)
    age = Column(Integer, nullable=False)
    planet = Column (Integer, ForeignKey('planets.id'))
    ships = relationship('Ships')
    user = relationship('User')
    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column (Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    persons = relationship('Characters')
    user = relationship('User')
    def to_dict(self):
        return {}

class Ships(Base):
    __tablename__='ships'
    id = Column (Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    size = Column(Integer, nullable=False)
    owner = Column(Integer, ForeignKey('characters.id'))
    user = relationship('User')
    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
