#!/usr/bin/env python
# coding=utf-8
from ossInit import oss

# 使用upload id取消分块上传事件
res =oss.cancel_upload('jingyun-test', 'wine-qqintl.zip', '3DC02690E53747F49B7FD9D55F8D3B06')
print "%s\n%s" % (res.status, res.read())

