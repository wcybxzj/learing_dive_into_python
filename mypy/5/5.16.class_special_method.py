#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Test(object):

	def __init__(self, dict=None):
		self.data = {}

	def __getitem__(self, name):
		"""docstring for __getitem__"""
		return self.data[name]

	def __setitem__(self, name ,val):
		"""docstring for __getitem__"""
		self.data[name] = val

	def __repr__(self):
		"""docstring for __repr__"""
		return 'this is from __repr'

	def __cmp__(self, dict):
		"""docstring for fname"""
		if isinstance(dict, Test):
			return cmp(self.data, dict.data)
		else:
			return cmp(self.data, dict)

	def __len__(self):
		return len(self.data)

	def __delitem__(self, key):
		"""docstring for __delitem"""
		del self.data[key]


t = Test()
t['name'] = 'ybx'
print t['name']
print t

print '-----------------------------'
t2 = Test()
t2['name'] = 'ybx'
print t == t2

d={}
d['name']= 'ybx'
print d == t2

print '-----------------------------'
print len(t2)

print '-----------------------------'
del t2['name']
print t2
