#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
	print 2

foo_doc = foo.__doc__
print foo_doc
print type(foo_doc)
print foo_doc == None
print foo_doc is None

print '==========================='

foo_doc_str = str(foo_doc)
print foo_doc_str
print type(foo_doc_str)
print foo_doc_str == None
