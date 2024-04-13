#!/usr/bin/python3
"""Module lists state all state objects"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access database and get states"""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    cal = State(name='California')
    san = City(name='San Fransisco')
    cal.cities.append(san)

    session.add(cal)
    session.commit()
    session.close()
