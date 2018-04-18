#!/usr/bin/env python
#encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Ksiazki(Base):
    __tablename__ = 'ksiazki'
    id = Column(Integer,primary_key=True)
    tytul = Column(String(100))
    autor = Column(String(100))
    rok_Wydania= Column(Integer)
    #ksiazkowanie = relationship('Wypozyczalnia', backref='ksiazki')
    
         
engine = create_engine('sqlite:///biblioteka1.db', echo = True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for ksiazka in session.query(Ksiazki).all():
    print(ksiazka.id, ksiazka.tytul, ksiazka.autor, ksiazka.rok_Wydania)
    
class Wypozyczalnia(Base):
    __tablename__ = 'wypozyczalnia'
    id = Column(Integer,primary_key=True)
    id_ksiazki = Column(Integer, ForeignKey('ksiazki.id'))
    id_Wypozyczajacego = Column(Integer, ForeignKey('daneOsobowe.id'))
    
class Dane(Base):
    __tablename__ = 'daneOsobowe'
    id = Column(Integer,primary_key=True)
    imie = Column(String(100))
    nazwisko = Column(String(100))
    #osoba = relationship('Wypozyczalnia', backref='daneOsobowe')

