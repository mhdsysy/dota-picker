import glob
import os

from numpy import genfromtxt
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class counters(Base):
    __tablename__ = 'counters'

    id = Column(Integer, primary_key=True)
    hero = Column(String(250), nullable=False)
    counter = Column(String(250), nullable=False)


# Create the database
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

# create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, dtype=None, encoding=None)
    return data.tolist()


try:
    current_path = os.getcwd()
    # Get list of files in folder
    files = glob.glob(os.path.join(current_path, "*.csv"))

    # Loop through all files in list
    for file_path in files:
        file_name = file_path.split('/')[-1]
        data = Load_Data(file_name)

        for i in data:
            record = counters(**{
                'hero': i[0],
                'counter': i[1]
            })
            s.add(record)
    s.commit()

except:

    s.rollback()  # Rollback the changes on error
finally:
    s.close()  # Close the connection
