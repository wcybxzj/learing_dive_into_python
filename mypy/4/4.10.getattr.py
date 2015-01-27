#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types
print "========getattr用于list============"
li = ["Larry", "Curly"]
print li.pop

print getattr(li, 'pop')

getattr(li, "append")("Moe")
print li

print "========getattr用于dict============"
print getattr({}, "clear")

print "========getattr不能用于tuple============"
try:
	getattr((), "pop")
except AttributeError:
	print '元组没有方法'
