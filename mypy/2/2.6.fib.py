#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    if n>1:
        num = n * fib(n-1)
        print num
        return n
    else:
        print 'end of the line'
        print 1
        return 1
fib(5)
