__author__ = 'wcybxzj'


params = {"server":"linux", "database":"mysql", "uid":100, "pwd":12345}

print "%(pwd)s is not good passsword for %(uid)s" % params




def handle_test(text):
    print "%(text)s" %locals()

handle_test("ybx")