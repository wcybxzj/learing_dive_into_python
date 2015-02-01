#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

fsock = open('error.log', 'w')
sys.stderr = fsock
raise Exception, 'this error will be logged'
