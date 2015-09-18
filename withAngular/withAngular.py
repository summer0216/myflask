#coding=utf-8
from flask import Flask,render_template,jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    jsonlist=['a','b','c','d']
    jsonstr=json.dumps(jsonlist)
    return render_template('index.html',jsonstr=jsonstr)


@app.route('/tpl3/')
def hello_world1():
    return render_template('tpl3.html')


@app.route('/tpl4/')
def hello_world2():
    return render_template('tpl4.html')


if __name__ == '__main__':
    app.run(debug=True)
