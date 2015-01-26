#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "----------list slice---------"
my_list = ['a', 'b', 'cc', 'dd', 'ee']
#第1个值是你想要的pos, 第2个是你不想要的pos
print my_list[1:3]
print my_list[1:-1]
print my_list[0:3]
print my_list[:3]
print my_list[3:]
print my_list[:]

print "-----append/insert/extend 都没有返回值----"
my_list.append('new')
print my_list
my_list.insert(2,'new')
print my_list
my_list.extend(["two", "element"])
print my_list

print "-------append vs extend-------"
li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
print li
print len(li)
print li[-1]
print '\n'
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
print li
print len(li)
print li[-1]

print "----------search in list---------"
li =['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
print li.index("example")
print li.index("new") #这里只能获取new第一次出现的位置
try:
    print li.index('11111111111')
except ValueError:
    print '不存在的值将会引起 ValueError'
if not "1111111111" in li:
    print '不存在此值'


print "----------remove 没有返回值---------"
li =['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove('z')
print li

try:
    li.remove('c')
except ValueError:
    print '删除一个不存在的数在list中'

li.pop()
print li

print "------------使用 list 的运算符---------"
li = ['a', 'b', 'mpilgrim']
li = li+['example', 'new']
print li

li += ['two']
print li

li = [1, 2] * 3
print li
