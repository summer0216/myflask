#!/usr/bin/env python
# coding=utf-8
from ossInit import oss

# 批量删除3个object
objectlist = [
    "Flask Web开发：基于Python的Web应用开发实战.pdf"
]
res = oss.batch_delete_objects("jingyun-upload", objectlist)
print "Is success?"
print res
