# coding=utf-8
from flask import Flask,render_template,json

app = Flask(__name__)

# custom filter
# convert dict to string
def json_dumps(dict):
        result = json.dumps(dict)
        return result
# return type of arg
def typeFilter(arg):
        result = type(arg)
        return result

env = app.jinja_env
env.filters['json_dumps'] = json_dumps
env.filters['typeFilter'] = typeFilter

@app.route('/')
def hello_world():
    dict={'name':'lewis','age':24}
    return render_template('index.html',dict=dict)


if __name__ == '__main__':
    app.run()
