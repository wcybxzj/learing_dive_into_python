#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "=======查看当前有什么模块========"
import sys, fileinfo
print "\n".join(sys.modules.keys()[:15])

print "=============fileinfo============="
print fileinfo
print sys.modules["fileinfo"]

print "====================================="
print "==通过__module__ 查看函数所属module=="
from fileinfo import MP3FileInfo
print MP3FileInfo.__module__
print sys.modules[MP3FileInfo.__module__]
