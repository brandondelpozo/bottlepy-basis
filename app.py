from bottle import run, route

@route('/')
def index():
    return '<hi>Game Over!</h1>'

if __name__ == '__main__':
    run