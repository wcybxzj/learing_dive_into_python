#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '推荐:from xxx import yyy, yyy就会导入到当前的作用域'
print """避免:from xxx import * 会造成名字冲突和掉是困难"""
print "============================================="
import types
print types.FunctionType

try:
    FunctionType
except Exception, e:
    print e
    print 'import 没有把命名空间导入到当前区域'

print "============================================="
from types import FunctionType
print FunctionType
