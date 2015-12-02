#!/usr/bin/env python
# coding=utf-8
from ossInit import oss

res = oss. delete_bucket('jingyun-upload')
print "%s\n%s" % (res.status, res.read())
