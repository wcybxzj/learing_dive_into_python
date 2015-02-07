#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = ('a', 'b', 'mpilgrim', 'z', 'example')

#1.tuple can not append
try:
    t.append("new")
except AttributeError:
    print 'tuple can not append'

print 'test after error'

#2.typle change to list
t_list = list(t)
t_list.append("1111")
print t_list

#3.in
if "z" in t:
    print 'have z in this tuple'

#4.tuple做list的key
list = {t:'121212'}
print list[t]
