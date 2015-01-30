#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ClassOne(object):
	def __init__(self, arg=None):
		pass

	def copy(self):
		if self.__class__ is ClassOne:
			print 'yes'
		else:
			print 'nonono'

class ClassChild(ClassOne):
	def callCopy(self):
		self.copy()

p = ClassOne()
p.copy()

c = ClassChild()
c.callCopy()


