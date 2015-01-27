#!/usr/bin/env python
# -*- coding: utf-8 -*-


import statsout

print statsout.output_html


def output(data, format="text"):
	try:
		func = getattr(statsout, "output_%s" % format)
	except AttributeError:
		print '模块中不存在此方法'
		return
	return func(data)

#getattr如果请求的方法不存在就会引起异常
#办法就是设置默认值
def output_better(data, format="text"):
	func = getattr(statsout, "output_%s" % format,
			statsout.output_text)
	return func(data)

output('111')
output('222', 'html')
output('222', 'no_exists')

output_better('222', 'no_exists')


