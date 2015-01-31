#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
print os.listdir(".")

print '=============glob 1=================='
import glob
print glob.glob('./*.py')

print '=============glob 2=================='
before_path = os.path.realpath('../..')
print before_path
pattern = before_path+'/mypy/*/*.1*.py'
print pattern
print glob.glob(pattern)
