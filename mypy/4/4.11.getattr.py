#!/usr/bin/env python
# -*- coding: utf-8 -*-

import odbchelper
import types

#getattr可以得到一个直到运行时才知道名称的函数的引用
print odbchelper.buildConnectionString
print getattr(odbchelper, "buildConnectionString")
object = odbchelper
method = "buildConnectionString"
print getattr(object, method)

print "==================================="
print type(getattr(object, method))
print type(getattr(object, method)) == types.FunctionType
print callable(getattr(object, method))
