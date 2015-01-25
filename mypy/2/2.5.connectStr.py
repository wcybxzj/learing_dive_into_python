#!/usr/bin/env python
# -*- coding: utf-8 -*-


def connectStr(params):
    list_iter = ["%s=%s" % (k, v) for k, v in params.items()];
    return ";".join(list_iter)

str= {'name':'ybx', 'sex':'male'}

print connectStr(str)
