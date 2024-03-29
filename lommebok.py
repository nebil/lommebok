"""
Copyright (c) 2016-2017, Nebil Kawas García
This source code is subject to the terms of the Mozilla Public License.
You can obtain a copy of the MPL at <https://www.mozilla.org/MPL/2.0/>.
"""

import database
from bottle import (get, post, redirect, static_file, request, template,
                    HTTPError, TEMPLATE_PATH,
                    hook, run)

ASSETS_REGEX = r'.*\.(css|svg)'
TEMPLATE_PATH.append('templates')


@get('/<filename:re:{}>'.format(ASSETS_REGEX))
def return_static_file(filename):
    return static_file(filename, root='assets')


@get('/')
def index():
    return template('index')


@get('/accounts/')
def get_accounts(database_conn):
    cursor = database_conn.execute("SELECT * FROM account")
    result = cursor.fetchall()
    return template('accounts', accounts=result)


@get('/accounts/<id_>/')
def get_account(database_conn, id_):
    id_ = tuple(id_)

    account_query = "SELECT * FROM account WHERE id=?"
    records_query = "SELECT * FROM record WHERE account_id=?"
    result = {'account': database_conn.execute(account_query, id_).fetchone(),
              'records': database_conn.execute(records_query, id_).fetchall()}

    if not result['account']: return HTTPError(404, "Invalid account.")
    return template('account', **result)


@post('/accounts/')
def add_account(database_conn):
    values = request.forms.get('name'), request.forms.get('currency')

    database_conn.execute("INSERT INTO account VALUES (NULL, ?, ?)", values)
    database_conn.commit()
    redirect('')


@post('/accounts/<account_id>/records/')
def add_record(database_conn, account_id):
    args = (request.forms.get('amount'), request.forms.get('created_on'),
            account_id)

    database_conn.execute("INSERT INTO record VALUES (NULL, ?, ?, ?)", args)
    database_conn.commit()
    redirect('..')


@hook('before_request')
def append_slash():
    if request.path.endswith(('/', '.css', '.svg')):
        pass
    else:
        redirect(request.path + '/')


if __name__ == '__main__':
    database.initialize()

    # Listening on 'localhost:8080' with the standard 'wsgiref' module.
    # More details at <https://docs.python.org/3/library/wsgiref.html>.
    run(host='localhost', port='8080', server='wsgiref', reloader=True)
