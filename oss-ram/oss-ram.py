# coding=utf-8
from flask import Flask, render_template, json
from aliyunsdkcore import client
from aliyunsdkram.request.v20150501 import CreateUserRequest, GetUserRequest, DeleteUserRequest, CreateAccessKeyRequest, \
    CreatePolicyRequest, AttachPolicyToUserRequest,DeleteAccessKeyRequest

app = Flask(__name__)


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
    request.set_UserName('alice')

    # 发起请求，并得到response
    response = clt.do_action(request)

    print response
    return response


@app.route('/get/')
def get():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = GetUserRequest.GetUserRequest()

        request.set_UserName('alice')
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
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

        request.set_UserName('alice')
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
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

        request.set_UserName('alice')
        request.get_UserName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


@app.route('/del_access/')
def del_access():
    try:
        # 构建一个 Aliyun Client, 用于发起请求
        # 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
        # RAM是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
        clt = client.AcsClient('QFmrMPB18qNx9KYc', 'IuAdh4qL9noDf0UnMOO977HSgZSc0E', 'cn-hangzhou')

        # 构造"CreateUser"请求
        request = DeleteAccessKeyRequest.DeleteAccessKeyRequest()

        request.set_UserName('alice')
        request.set_UserAccessKeyId('gSSLC8y4X3LPuyMe')

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
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

        request.set_PolicyName('alice_policy')

        policy_document = json.dumps({
            "Statement": [
                {
                    "Action": [
                        "oss:PutObject",
                        "oss:AbortMultipartUpload"
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "acs:oss:*:*;jingyun-shenzhen",
                        "acs:oss:*:*:jingyun-shenzhen/users/alice/*"
                    ]
                }
            ],
            "Version": "1"
        })

        request.set_PolicyDocument(policy_document)

        request.get_PolicyName()

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
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
        request.set_PolicyName('alice_policy')
        request.set_UserName('alice')

        # 发起请求，并得到response
        response = clt.do_action(request)

        print response
        return response
    except Exception, e:
        print(e.args)
        error_message = str(e.args)
        return error_message


if __name__ == '__main__':
    app.run()
