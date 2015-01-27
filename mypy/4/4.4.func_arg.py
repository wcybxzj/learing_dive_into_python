#!/usr/bin/env python
# -*- coding: utf-8 -*-

def func(a=1, b=2):
	"""docstring for func"""
	print 'a:%s'% a
	print "b:%s" % b

if __name__ == '__main__':
	func()
	print '==============='
	func(b=3)
