#!/usr/bin/python3
"""
This script lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get states
    that contain the letter 'a'.
    """

    # Create the database URL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create the engine
    engine = create_engine(db_url)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    # Query the database for states containing the letter 'a' and sort by id
    states = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()
    
    # Print the results
    for state in states:
        print(f'{state.id}: {state.name}')
    
    # Close the session
    session.close()
