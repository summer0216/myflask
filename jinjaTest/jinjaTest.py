from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap= Bootstrap(app)


@app.route('/')
def hello_world():
    name=u'name';
    print name
    user_info={u'name':u"lewis",u"age":u"23",u"sex":u"male"}
    return render_template("index.html",user_info=user_info)


if __name__ == '__main__':
    app.run(port=5001)
