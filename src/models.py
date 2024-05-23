
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False,unique=True)
    passport = Column(String(12), nullable=False,unique=True)

    def serialize(self):
        return {
            'id ':self.id,
            'name' :self.name,
            'passport': self.passport
        }

class Planets(Base):
    __tablename__ = 'planets'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(25),nullable=False,unique=True)

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name
        }

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(25),nullable=False,unique=True)
    planet = Column(String(25),ForeignKey(Planets.name))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'planet': self.planet
        }
    
class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key = True)
    User_id = Column(Integer, ForeignKey(User.id))
    Planets_id = Column(Integer, ForeignKey(Planets.id))
    People_id = Column(Integer, ForeignKey(People.id))


         



    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
