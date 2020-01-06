import pandas as pd
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Map which table in database will be related to each class
Base = declarative_base()

class counters(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    hero_name = Column(String(250),nullable=False)
    counters = Column(String(250),nullable=False)


engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)



# Read file into dataframe
csv_data = pd.read_csv('data.csv')

# Convert dataframe to list and store in same variable



# Use table_definition function to define table structure
# Loop through list of lists, each list in create_bom_table.xls_data is a row
for row in csv_data:
# Each element in the list is an attribute for the table class
# Iterating through rows and inserting into table


