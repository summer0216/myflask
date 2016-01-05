#!/usr/bin/env python
# coding=utf-8
import oss2
from itertools import islice

accessKeyId, accessKeySecret = "QFmrMPB18qNx9KYc", "IuAdh4qL9noDf0UnMOO977HSgZSc0E"
endpoint = "http://oss-cn-beijing.aliyuncs.com"

auth = oss2.Auth(accessKeyId, accessKeySecret)
bucket = oss2.Bucket(auth, endpoint, 'jingyun-upload')

for b in islice(oss2.ObjectIterator(bucket), 10000):
    print(b.key)
