#!/usr/bin/env python
# -*- coding: utf-8 -*-


def buildConnectionString(params):
    list_iter = ["%s=%s" % (k, v) for k, v in params.items()];
    return ";".join(list_iter)

if __name__ == '__main__':
	str= {'name':'ybx', 'sex':'male'}
	print buildConnectionString(str)
