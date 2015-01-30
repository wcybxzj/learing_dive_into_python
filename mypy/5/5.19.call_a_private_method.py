#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    私有函数不可以从它们的模块外面被调用(不理解)
    私有类方法不能够从它们的类外面被调用
    私有属性不能够从它们的类外面被访问
"""

class Student:
    def fname(self):
        """docstring for fname"""
        return 'work'

    def __p1func__(self):
        print 'p1'

    def __p2func(self):
        """docstring for __p2func"""
        print 'p2'

#s = Student()
#print s.fname()
#print s.__p1func__()
#print s.__p2func()

import fileinfo
info = fileinfo.MP3FileInfo()
info.__setitem__('name', './123.mp3')
print info.test()

try:
    print info.__private_func()
except AttributeError:
    print '只有两个斜线开头的是私有方法'

try:
    print info.__public_func2__()
except AttributeError:
    print '__public_func2__ 是一个公共方法'

try:
    print info.__private_var
except AttributeError:
    print '不能访问私有属性'

print "强制访问私有属性"
print info._MP3FileInfo__private_var

print info.__public_var__
