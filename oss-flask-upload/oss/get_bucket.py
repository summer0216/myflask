#!/usr/bin/env python
# coding=utf-8
import oss2
from itertools import islice

accessKeyId, accessKeySecret = "QFmrMPB18qNx9KYc", "IuAdh4qL9noDf0UnMOO977HSgZSc0E"
endpoint = "http://oss-cn-beijing.aliyuncs.com"

auth = oss2.Auth(accessKeyId, accessKeySecret)
bucket = oss2.Bucket(auth, endpoint, 'jingyun-upload')

files = []


def digui(pre, parent):
    for obj in oss2.ObjectIterator(bucket, delimiter='/', prefix=pre):
        array=obj.key.split("/")
        if array[-1] is "":
            parent.append({"text": array[-2], "children": []})
        else:
            parent.append({"text": array[-1], "children": []})
        if obj.is_prefix():  # 文件夹
            digui(obj.key, parent[-1]["children"])


digui('',files)
print(files)