from bottle import get, run


@get('/')
def index():
    return "Bienvenido a Lommebok."


# Listening on 'localhost:8080' with the standard 'wsgiref' module.
# More details at <https://docs.python.org/3/library/wsgiref.html>.
run(host='localhost', port='8080', server='wsgiref', reloader=True)
