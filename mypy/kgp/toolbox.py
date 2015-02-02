__author__ = 'yangbingxi'


def openAnything(source):
    """
    >>> from xml.dom import minidom
    >>> sock = openAnything("http://localhost/kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("c:\\inetpub\\wwwroot\\kant.xml")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    >>> sock = openAnything("<ref id='conjunction'><text>and</text><text>or</text></ref>")
    >>> doc = minidom.parse(sock)
    >>> sock.close()
    """
    if hasattr(source, "read"):
        return source

    if source == "-":
        import sys
        return  sys.stdin

    import urllib
    try:
        return urllib.urlopen(source)
    except(IOError, OSError, ValueError):
        pass

    try:
        return open(source)
    except(IOError, OSError):
        pass

    import StringIO
    return StringIO.StringIO(str(source))



