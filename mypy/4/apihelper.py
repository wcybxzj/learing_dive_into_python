#!/usr/bin/env python
# -*- coding: utf-8 -*-

def info(object, spacing=10, collapse=1):
	"""Print methods and doc strings.

	Takes module, class, list, dictionary, or string."""
	methodList=[method for method in dir(object) \
		if callable(getattr(object, method))]

	processFunc = collapse and \
		( lambda s:" ".join( s.split() ) )  or \
		(lambda s: s)

	print "\n".join(["%s %s" % \
		(method.ljust(spacing),
			processFunc(str(getattr(object, method).__doc__))
		)
		for method in methodList])


class myclass(object):
	"""docstring for myclass"""
	def fname(self):
		"""0000000000

		1111111111111"""
		pass

	def test(self):
		return 123

if __name__ == '__main__':
	li = []
	info(li, 30)
	print '==========================='
	info(li, 30, 0)
	print '==========================='
	my_obj = myclass()
	info(my_obj, 30, 0)
