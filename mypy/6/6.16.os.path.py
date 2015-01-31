#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
print '==========os.path.join()============'
current_user_dir = os.path.expanduser("~")
all_path = os.path.join(current_user_dir, '123.php')
print all_path

print '==========os.path.split()============'
(filepath, filename) = os.path.split(all_path)
print filepath
print filename

print '==========os.path.splitext()========='
(shortname, extension) = os.path.splitext(filename)
print shortname
print extension

print "=========os.listdir()================"
current_dir = os.path.realpath('.')
print os.listdir(current_dir)

print "=============输出文件================"
print [file for file in os.listdir(current_dir)
		if os.path.isfile(os.path.join(current_dir, file))]

print "=============输出目录================"
before_dir = os.path.realpath('..')
print str(type(before_dir)) + " " + before_dir
print [item for item in os.listdir(before_dir)
		if os.path.isdir(os.path.join(before_dir, item))]

print "====想看一下os.path.join的是否可以被取代===="
if os.path.isdir(os.path.join(before_dir, item)):
	print 'is dir'

if os.path.isdir(before_dir+'/'+item):
	print 'is dir'

print os.path.join(before_dir, item)
print before_dir+item
