#!/usr/bin/env python
# coding=utf-8
from ossInit import oss

# 使用upload id取消分块上传事件
res =oss.cancel_upload('jingyun-upload', '2015-S06084_R2.fq.gz', '42415CC93945486DB9D01759D93C1467')
print "%s\n%s" % (res.status, res.read())

