from flask import Flask, render_template,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField("what's your name?", validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html',form=form,name=name)

@app.route('/load/', methods=['GET', 'POST'])
def load():
    print(request.form["name"])
    return "<div>617</div>"

if __name__ == '__main__':
    app.run(port=8001)
