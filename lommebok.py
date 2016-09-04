from bottle import get, run


@get('/')
def index():
    return "Bienvenido a Lommebok."


run()
