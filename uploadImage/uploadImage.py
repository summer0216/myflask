# coding:utf-8
from flask import Flask, render_template, request, url_for
import os, sys

app = Flask(__name__)

image_path = os.path.join(sys.path[0], 'static')


@app.route('/')
def hello():
    return render_template('index1.html')



@app.route('/upload', methods=['POST'])
def upload_file():
    image_path = os.path.join(sys.path[0], 'static')
    image = request.files['file']
    image.save(os.path.join(image_path, image.filename))
    imgHtml = '<img src="' + url_for('static', filename=image.filename) + '"/>'
    return imgHtml

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
