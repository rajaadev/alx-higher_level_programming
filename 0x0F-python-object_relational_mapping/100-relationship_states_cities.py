#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco" from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cali = State(name="California")
    city = City(name="San Francisco")
    cali.cities.append(city)

    session.add(cali)
    session.commit()

    session.close()
