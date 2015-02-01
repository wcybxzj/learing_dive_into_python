#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '=============locals()================'
def foo(arg):
    """docstring for foo"""
    x=1
    print locals()

foo(7)
foo('bar')

print '=============globals()================'

class ClassOne(object):
    """docstring for ClassOne"""
    def __init__(self, arg):
        super(ClassOne, self).__init__()
        self.arg = arg

class ClassTwo(object):
    """docstring for ClassTwo"""
    def __init__(self, arg):
        super(ClassTwo, self).__init__()
        self.arg = arg

for k, v in globals().items():
    print k ,'=', v
