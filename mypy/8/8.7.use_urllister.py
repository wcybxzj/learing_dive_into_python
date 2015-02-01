__author__ = 'wcybxzj'

import urllib, urllister

uscok = urllib.urlopen("http://www.baidu.com")
parser = urllister.URLLister()
parser.feed(uscok.read())
uscok.close()
parser.close()

for url in parser.urls:
    print url