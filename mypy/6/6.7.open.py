#!/usr/bin/env python
# -*- coding: utf-8 -*-


#print "w,不存在就会创建,存在就会覆盖原有文件"
#logfile = open('test.log', 'w')
#logfile.write('test succeeded')
#logfile.close()
#print file('test.log').read()

print 'a,不存在就创建,存在就添加'
logfile = open('test.log', 'a')
logfile.write('line2')
logfile.close()
print file('test.log').read()
