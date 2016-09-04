import sqlite3
from lommebok import DATABASE_PATH

# Reference: <https://www.sqlite.org/datatype3.html>
QUERY = """
        CREATE TABLE account(id INTEGER PRIMARY KEY, name TEXT, currency TEXT);
        """

database_conn = sqlite3.connect(DATABASE_PATH)

try:
    database_conn.execute(QUERY)
except sqlite3.OperationalError as error:
    message = "error -- {}".format(error)
    print(message)
else:
    database_conn.commit()
finally:
    database_conn.close()
