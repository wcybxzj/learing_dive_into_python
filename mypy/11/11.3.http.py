__author__ = 'yangbingxi'

import httplib

httplib.HTTPConnection.debuglevel = 1

import urllib
feeddata = urllib.urlopen('http://localhost/binary.xml').read()
print feeddata