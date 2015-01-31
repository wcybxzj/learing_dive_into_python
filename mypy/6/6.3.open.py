#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('6.2.support_special_platform.py',\
        'rb')
print f
print f.mode
print f.name
print f.tell()

print '================='
f.seek(-128, 2)
print f.tell()
print f.read(10)
print f.tell()

print '================='
print f.closed
f.close()
print f.closed

try:
    f.tell()
except ValueError:
    print '文件不存在不能操作'
