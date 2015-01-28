#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = 'first'
b = 'second'

print '=================4.17======================'
print 1 and a or b
print 0 and a or b

print '==========4.18期望得到a 但是得到b========'
print '==========问题就出在a 被判定为false======'
a = ""
b ="second"
print 1 and a or b

print "==============4.19最佳实践==============="
a = ""
b ="second"
c = 0
print (1 and [a] or [b])[0]
print (1 and [c] or [b])[0]
