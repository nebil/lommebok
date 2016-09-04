import sqlite3
from bottle import get, post, redirect, request, run, template

DATABASE_PATH = 'lommebok.sqlite3'
database_conn = sqlite3.connect(DATABASE_PATH)
database_conn.row_factory = sqlite3.Row


@get('/')
def index():
    return template('index')


@get('/accounts/')
def get_accounts():
    cursor = database_conn.execute("SELECT * FROM account")
    result = cursor.fetchall()
    return template('accounts', accounts=result)


@post('/accounts/')
def add_account():
    values = request.forms.get('name'), request.forms.get('currency')

    database_conn.execute("INSERT INTO account VALUES (NULL, ?, ?)", values)
    database_conn.commit()
    redirect('')


if __name__ == '__main__':
    # Listening on 'localhost:8080' with the standard 'wsgiref' module.
    # More details at <https://docs.python.org/3/library/wsgiref.html>.
    run(host='localhost', port='8080', server='wsgiref', reloader=True)
