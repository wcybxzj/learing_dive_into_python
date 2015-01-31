#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    fsock = open("/nothave.txt", "r")
except IOError:
    print '异常被捕捉程序继续执行'

print '如果不捕捉异常,下面的程序无法继续执行'
fsock = open("/nothave.txt", "r")
print '1111111111'
