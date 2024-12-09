import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), unique = True, nullable = False)
    email = Column(String(250), unique = True, nullable = False)
    password = Column(String(250), nullable = False)


class Favorite_Character(Base):
    __tablename__ = 'favoritecharacter'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(250), nullable = False)
    characteristics = Column(Text)
    id_user = Column(Integer, ForeignKey("user.id"), nullable = False)


favorite_character = Table(
    "favorite_character",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key = True, nullable = False),
    Column("character_id", Integer, ForeignKey("planet.id"), primary_key = True, nullable = False)
)

favorite_planet = Table(
    "favorite_planet",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key = True, nullable = False),
    Column("planet_id", Integer, ForeignKey("planet.id"), primary_key = True, nullable = False)
)
    
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True, autoincrement= True)
    name = Column(String(250), nullable = False, unique = True)
    characteristics = Column(Text)
    habitable = Column(Boolean, default = True, comment = "true = habitable false = no habitable")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(250), nullable = False, unique = True)
    characteristics = Column(Text)


    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
