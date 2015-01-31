#!/usr/bin/env python
# -*- coding: utf-8 -*-
for i in range(5):
	print i

print "======================"
print "======================"

li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
	print li[i]

print "======================="
print "=========for============"
import os
for k,v in os.environ.items()[:3]:
	print "%s=%s" % (k, v)

print "====================================="
print "==========list comprehension========="
print "\n".join(["%s=%s" % (k, v) \
		for k, v in os.environ.items()[:3]])


