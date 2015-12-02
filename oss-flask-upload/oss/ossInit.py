#!/usr/bin/env python
# coding=utf-8
from oss.oss_api import *

endpoint = "oss-cn-beijing.aliyuncs.com"
accessKeyId, accessKeySecret = "QFmrMPB18qNx9KYc", "IuAdh4qL9noDf0UnMOO977HSgZSc0E"

oss = OssAPI(endpoint, accessKeyId, accessKeySecret)