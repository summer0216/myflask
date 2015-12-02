#!/usr/bin/env python
# coding=utf-8
from flask import Flask,render_template,jsonify
from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest
import xmltodict

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('demo.html')


@app.route('/token', methods=['GET', 'POST'])
def get_token():
    # 构建一个 Aliyun Client, 用于发起请求
    # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
    # STS是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
    clt = client.AcsClient('7INC3dZeicoD76fh', 'OEXsOXyiMqxNY80jLGGXryM6riMrni', 'cn-beijing')

    # 构造"AssumeRole"请求
    request = AssumeRoleRequest.AssumeRoleRequest()
    # 指定角色
    request.set_RoleArn('acs:ram::20199148:role/role-oss-js-upload')
    # 设置会话名称，审计服务使用此名称区分调用者
    request.set_RoleSessionName('jingyun')

    # 发起请求，并得到response
    response = clt.do_action(request)

    dict=xmltodict.parse(response)

    return jsonify(dict['AssumeRoleResponse'])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8081)
