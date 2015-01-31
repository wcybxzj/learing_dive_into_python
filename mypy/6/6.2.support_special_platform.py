#!/usr/bin/env python
# -*- coding: utf-8 -*-
import getpass

try:
	import termios, TERMIOS
except ImportError:
	try:
		import msvcrt
	except ImportError:
		try:
			from EasyDialogs import AskPassword
		except ImportError:
			getpass = getpass.getpass()
		else:
			getpass = AskPassword
	else:
		getpass = win_getpass
else:
	get_pass = unix_getpass
finally:
	print 'success!'
