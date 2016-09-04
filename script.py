import sqlite3

# Reference: <https://www.sqlite.org/datatype3.html>
QUERY = """
        CREATE TABLE account(id INTEGER PRIMARY KEY, name TEXT, currency TEXT);
        """

database_conn = sqlite3.connect('lommebok.sqlite3')

try:
    database_conn.execute(QUERY)
except sqlite3.OperationalError:
    print("error")
else:
    database_conn.commit()
finally:
    database_conn.close()
