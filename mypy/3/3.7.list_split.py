#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1.join 只能连接字符串值的列表
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
list_c = ["%s=%s" % (k, v) for k, v in params.items()]
print ";".join(list_c)

#2.split
print "================2.split==========================="
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print s

s = s.split(";", 1)
print s
