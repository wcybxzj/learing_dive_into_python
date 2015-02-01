__author__ = 'wcybxzj'

from xml.dom import minidom
xmldoc = minidom.parse('../kgp/binary.xml')
#print xmldoc.toxml()
print xmldoc.childNodes
print xmldoc.childNodes[0]
print xmldoc.firstChild
