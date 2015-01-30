#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinfo

f = fileinfo.FileInfo('./123.mp3')
print f

print f['name']
print f.__getitem__("name")

f['sex'] = '男'
print f['sex']
print f.__getitem__("sex")
