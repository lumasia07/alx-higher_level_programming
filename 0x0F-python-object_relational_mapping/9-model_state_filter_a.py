#!/usr/bin/python3
"""Module lists state all state objects"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access database and get states"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    a_state = session.query(State).filter(State.name.contains('a'))

    if a_state is not None:
        for state in a_state:
            print('{0}: {1}'.format(state.id, state.name))
