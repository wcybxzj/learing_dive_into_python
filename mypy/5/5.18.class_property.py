#!/usr/bin/env python
# -*- coding: utf-8 -*-

#类属性
class counter:
    count = 0
    def __init__(self):
        """docstring for __init__"""
        self.__class__.count += 1

print counter.count

c = counter()
print counter.count
print c.count

d = counter()
print d.count
print counter.count
