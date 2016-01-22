# coding=utf-8
from flask import Flask, render_template, json, jsonify,request
from aliyunsdkcore import client
from aliyunsdkram.request.v20150501 import CreateUserRequest, GetUserRequest, DeleteUserRequest, CreateAccessKeyRequest, \
    CreatePolicyRequest, AttachPolicyToUserRequest, DeleteAccessKeyRequest, DeletePolicyRequest, \
    DetachPolicyFromUserRequest, ListAccessKeysRequest
import xmltodict

import oss2

app = Flask(__name__)

user_name = 'JingYun'


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/add/')
def add():
    # 构建一个 Aliyun Client, 用于发起请求
    # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
    # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
    clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

    # 构造"CreateUser"请求
    request = CreateUserRequest.CreateUserRequest()
    # 设置参数 - UserName
    request.set_UserName(user_name)

    # 发起请求，并得到response
    response = clt.do_action(request)

    convertedDict = xmltodict.parse(response)

    return jsonify(convertedDict)


@app.route('/get/')
def get():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = GetUserRequest.GetUserRequest()

        request.set_UserName(user_name)
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/delete/')
def delete():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = DeleteUserRequest.DeleteUserRequest()

        request.set_UserName(user_name)
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)

    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/create_access/')
def create_access():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = CreateAccessKeyRequest.CreateAccessKeyRequest()

        request.set_UserName(user_name)
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)

    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/list_access/')
def list_access():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = ListAccessKeysRequest.ListAccessKeysRequest()

        request.set_UserName(user_name)

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)

    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/del_access/', methods=["POST"])
def del_access():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        req = DeleteAccessKeyRequest.DeleteAccessKeyRequest()

        req.set_UserName(user_name)
        req.set_UserAccessKeyId(request.form["access_id"])

        # 发起请求，并得到response
        response = clt.do_action(req)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/create_policy/')
def create_policy():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = CreatePolicyRequest.CreatePolicyRequest()

        request.set_PolicyName(user_name + '_policy')

        policy_document = json.dumps({
            "Version": "1",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "oss:ListBuckets"
                    ],
                    "Resource": [
                        "acs:oss:*:*:*"
                    ]
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "oss:PutObject"
                    ],
                    "Resource": [
                        "acs:oss:*:*:jingyun-users/" + user_name + "/*"
                    ]
                },
                {
                    "Effect": "Allow",
                    "Action": [
                        "oss:ListObjects"
                    ],
                    "Resource": [
                        "acs:oss:*:*:jingyun-users"
                    ],
                    "Condition": {
                        "StringLike": {
                            "oss:Delimiter": "/",
                            "oss:Prefix": ["",
                                           user_name + "/*"
                                           ]
                        }
                    }
                }
            ]
        })

        request.set_PolicyDocument(policy_document)

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/bind/')
def bind():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = AttachPolicyToUserRequest.AttachPolicyToUserRequest()

        request.set_PolicyType('Custom')
        request.set_PolicyName(user_name + '_policy')
        request.set_UserName(user_name)

        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/detach/')
def detach():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        request = DetachPolicyFromUserRequest.DetachPolicyFromUserRequest()

        request.set_PolicyType('Custom')
        request.set_PolicyName(user_name + '_policy')
        request.set_UserName(user_name)


        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/del_policy/')
def del_policy():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = DeletePolicyRequest.DeletePolicyRequest()

        request.set_PolicyName(user_name + '_policy')


        # 发起请求，并得到response
        response = clt.do_action(request)

        convertedDict = xmltodict.parse(response)

        return jsonify(convertedDict)
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/addFolder/')
def add_folder():
    try:
        auth = oss2.Auth('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E')
        bucket = oss2.Bucket(auth, 'oss-cn-shenzhen.aliyuncs.com', 'jingyun-users')

        result = bucket.put_object(user_name + "/readme.txt", "this is your folder,you can upload data to this,thanks")

        return jsonify({"status": result.status})
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


if __name__ == '__main__':
    app.run(port=8017)
