#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinfo
f = fileinfo.FileInfo("./123.mp3")
print f.__class__
print f.__doc__
print dir(fileinfo)
