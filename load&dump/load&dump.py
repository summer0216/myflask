from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/getstr/', methods=["GET"])
def hello_getstr():
    dic = {"name": "lewis", "age": "12", "sex": "man"}
    json_str = json.dumps(dic)
    return json_str

@app.route('/getjson/', methods=["GET"])
def hello_getjson():
    json_text = '{"name":"lewis","age":"12","sex":"man"}'
    json_dic = json.loads(json_text)
    json_str=json.dumps(json_dic)
    return json_str

if __name__ == '__main__':
    app.run(debug="true")
