import sqlite3

# Reference: <https://www.sqlite.org/datatype3.html>
QUERY = """
        CREATE TABLE account(id INTEGER PRIMARY KEY, name TEXT, currency TEXT);
        """

database_conn = sqlite3.connect('lommebok.sqlite3')
database_conn.execute(QUERY)
database_conn.commit()
database_conn.close()
