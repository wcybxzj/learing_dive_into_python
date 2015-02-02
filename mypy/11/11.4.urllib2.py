__author__ = 'yangbingxi'
import httplib


httplib.HTTPConnection.debuglevel = 1

import urllib2
request = urllib2.Request('http://localhost/binary.xml')
opener = urllib2.build_opener()
firststream = opener.open(request)

print firststream.headers.dict
request.add_header('If-Modified-Since',
                   firststream.headers.get('Last-Modified'))

import openanything
opener = urllib2.build_opener(
    openanything.DefaultErrorHandler()
)

seconddata = opener.open(request)
print seconddata.status


print '===================etag test======================'
print seconddata.headers.get('ETag')
firstdata =  firststream.read()
print firstdata
