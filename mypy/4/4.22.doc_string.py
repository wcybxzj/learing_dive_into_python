#!/usr/bin/env python
# -*- coding: utf-8 -*-

import odbchelper

object = odbchelper
method = 'buildConnectionString'
print getattr(object, method).__doc__
print type(getattr(object,'test').__doc__)
print type(str(getattr(object,'test').__doc__))
