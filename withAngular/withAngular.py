#coding=utf-8
from flask import Flask,render_template,jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    jsonlist=['a','b','c','d']
    jsonstr=json.dumps(jsonlist)
    return render_template('index.html',jsonstr=jsonstr)


if __name__ == '__main__':
    app.run(debug=True)
