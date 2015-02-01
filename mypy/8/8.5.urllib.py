__author__ = 'wcybxzj'
import urllib

sock = urllib.urlopen("http://www.baidu.com")
print sock.read()
sock.close()
