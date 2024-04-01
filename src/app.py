import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydatabase.db')


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# Define your SQL statements to create tables
sql_statements = [
    "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)",
    "CREATE TABLE IF NOT EXISTS Orders (id INTEGER PRIMARY KEY, user_id INTEGER, total_amount REAL)"
]

# Execute the SQL statements to create tables
with engine.connect() as connection:
    for statement in sql_statements:
        connection.execute(statement)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
with engine.connect() as connection:
    connection.execute("INSERT INTO your_table_name (column1, column2) VALUES ('value1', 'value2')")


# 4) Use pandas to print one of the tables as dataframes using read_sql function
    df = pd.read_sql("SELECT * FROM your_table_name", engine)
print(df)