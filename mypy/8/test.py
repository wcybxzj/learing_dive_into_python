__author__ = 'wcybxzj'

def func(tag):
    my_dic = {"name":"ybx", "age":"22"}
    strattrs = "".join([' %s="%s"' % (key,value)
                        for key, value in my_dic.items()])
    print locals()
    print "<%(tag)s%(strattrs)s>" % locals()

func('hahah')
