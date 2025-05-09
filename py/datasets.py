# Build datasets
import sqlite3
import pandas as pd
import numpy as np

# Chapter 6
## SQL database
ch6_query = """
CREATE TABLE test
(
    a VARCHAR(20),
    b VARCHAR(20),
    c REAL,
    d INTEGER
);
"""

## Start connection, execute and commit query
ch6_con = sqlite3.connect("examples/mydata.sqlite")
ch6_con.execute(ch6_query)
ch6_con.commit()
ch6_con.close()

# Insert data into db
## Build data and query
ch6_data = [
    ("Atlanta", "Georgia", 1.25, 6),
    ("Tallahassee", "Florida", 2.6, 3),
    ("Sacramento", "California", 1.7, 5),
]

ch6_query = "INSERT INTO test VALUES(?, ?, ?, ?)"

## Execute and commit query
ch6_con = sqlite3.connect("examples/mydata.sqlite")
ch6_con.executemany(ch6_query, ch6_data)
ch6_con.commit()
ch6_con.close()
