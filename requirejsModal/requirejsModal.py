# coding=utf-8
from flask import Flask, render_template, jsonify, request
import sys

reload(sys)
sys.setdefaultencoding('utf8')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/update/project/', methods=["post"])
def update_project():
    pro_name = request.form['pro_name']
    pro_description = request.form['pro_description']
    return jsonify({"status": 2, "message": "更新成功！项目名称、描述更新为:" + pro_name + "," + pro_description})


if __name__ == '__main__':
    app.run(debug=True)
