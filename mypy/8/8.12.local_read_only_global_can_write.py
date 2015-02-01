#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "locals 只读"
def foo():
	x = 1
	print locals()
	locals()["x"] = 2
	print "x=", x

foo()

print 'globals 可写'
z = 7
print 'z=', z
globals()["z"] = 100
print 'z=', z
