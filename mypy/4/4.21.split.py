#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "this is\na\ttest"
print s

print "===不带参数的 split 按照空白进行分割。\n \
所以三个空格、一个回车和一个制表符都是一样的。===="
print s.split()

print "==先把各种空格统一话,然后在以为单个空格进行连接=="
print " ".join(s.split())
