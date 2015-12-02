#!/usr/bin/env python
# coding=utf-8
from ossInit import oss

# 批量删除3个object
objectlist = [
    "阿里云消息队列服务(MQS)API文档.pdf",
    "大提琴头像.jpg",
    "wine-qqintl.zip",
    "umeditor1_2_2-src.zip",
    "ubuntukylin-14.04.1-desktop-amd64 (1).iso",
    "9.jpg",
    "1.jpg",
    "oss/folder/file_key"
]
res = oss.batch_delete_objects("jingyun-test", objectlist)
print "Is success?"
print res
