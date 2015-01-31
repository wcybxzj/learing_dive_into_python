#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	try:
		f = open("nothave.txt", "rb")
	finally:
		print '保证open后一定close'
		f.close()
except Exception, e:
	print e
