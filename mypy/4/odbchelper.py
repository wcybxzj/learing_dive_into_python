#!/usr/bin/env python
# -*- coding: utf-8 -*-


def buildConnectionString(params):
	"""that would be great"""
	list_iter = ["%s=%s" % (k, v) for k, v in params.items()];
	return ";".join(list_iter)

def test():
	return 11

if __name__ == '__main__':
	str= {'name':'ybx', 'sex':'male'}
	print buildConnectionString(str)
