import sqlite3
from lommebok import DATABASE_PATH

# Reference: <https://www.sqlite.org/datatype3.html>
QUERIES = """
          CREATE TABLE IF NOT EXISTS account(
            id INTEGER PRIMARY KEY,
            name TEXT,
            currency TEXT);

          CREATE TABLE IF NOT EXISTS record(
            id INTEGER PRIMARY KEY,
            amount INTEGER,
            created_on TEXT,
            account_id INTEGER,
            FOREIGN KEY(account_id) REFERENCES account(id));
          """

database_conn = sqlite3.connect(DATABASE_PATH)
database_conn.executescript(QUERIES)
database_conn.commit()
database_conn.close()
