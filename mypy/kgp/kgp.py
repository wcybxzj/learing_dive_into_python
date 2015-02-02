from xml.dom import minidom
import toolbox
import sys

class KantGenerator:
    def _load(self, source):
        sock = toolbox.openAnything(source)
        xmldoc =  minidom.parse(sock).documentElement
        sock.close()
        return xmldoc

    def work(self, source):
        return self._load(source)

k = KantGenerator()
print k.work('./kant.xml')
