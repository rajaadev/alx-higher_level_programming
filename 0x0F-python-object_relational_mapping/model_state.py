#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states"""

    __tablename__ = 'states'

    # Class attribute id representing a column of an auto-generated, unique integer, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Class attribute name representing a column of a string with maximum 128 characters, not null
    name = Column(String(128), nullable=False)
