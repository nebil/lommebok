"""
Copyright (c) 2016, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

import sqlite3

PATH = 'lommebok.sqlite3'

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


def initialize():
    database_conn = sqlite3.connect(PATH)
    database_conn.executescript(QUERIES)
    database_conn.commit()
    database_conn.close()
