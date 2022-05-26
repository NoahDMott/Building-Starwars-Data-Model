import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class StarWarsBlog(Base):
    __tablename__ = 'blog'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    HomePage = Column(String, nullable=False)
    CharacterInformationCard = Column(String, nullable=False)
    
class User(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'User'
    UserName = Column(String, nullable=False)
    email= Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    StarWarsBlog = relationship(StarWarsBlog)
    
class Favorite(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'Favorite'
    FavoriteCharacter = Column(String, nullable=True)
    FavoritePlant = Column(String, nullable=True)
    User = relationship(User)

class Character(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'Character'
    CharacterName = Column(String, nullable=False)
    CharacterPlanet = Column(String, nullable=False)
    CharacterBio = Column(String(500), nullable=False)
    StarWarsBlog = relationship(StarWarsBlog)

class Planet(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'Planet'
    PlanetName = Column(String, nullable=False)
    PlanetCharacter = Column(String(100), nullable=False)
    PlanetBio = Column(String(500), nullable=False)
    planet = relationship(StarWarsBlog)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')