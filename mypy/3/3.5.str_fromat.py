#!/usr/bin/env python
# -*- coding: utf-8 -*-

uid ="sa"
pwd = "secret"
# 两种方式结构完全相同
print pwd +' is password '+ uid
print '%s is password %s' % (pwd, uid)

userCount = 6
print "User connected:%d" % (userCount)

try:
	print "User connected" + userCount
except TypeError:
	print 'int cant connect with str'

#数值的格式化
print "Today's stock price:%f" % 50.4625
print "Today's stock price:%.2f" % 50.4625
print "Today's stock price:%+.2f" % 1.5
