from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'this is server'


@app.route('/api/')
def api():
    return 'api'


if __name__ == '__main__':
    app.run(port=5001)
