import sqlite3
from lommebok import DATABASE_PATH

# Reference: <https://www.sqlite.org/datatype3.html>
QUERIES = """
          CREATE TABLE account(id INTEGER PRIMARY KEY,
                               name TEXT,
                               currency TEXT);

          CREATE TABLE record(id INTEGER PRIMARY KEY,
                              amount INTEGER,
                              created_on TEXT,
                              account_id INTEGER,
                              FOREIGN KEY(account_id) REFERENCES account(id));
          """

database_conn = sqlite3.connect(DATABASE_PATH)

try:
    database_conn.executescript(QUERIES)
except sqlite3.OperationalError as error:
    message = "error -- {}".format(error)
    print(message)
else:
    database_conn.commit()
finally:
    database_conn.close()
