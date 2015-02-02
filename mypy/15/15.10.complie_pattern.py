__author__ = 'wcybxzj'
import re
pattern = '^M?M?M?$'
print re.search(pattern, 'M')

# 在需要多次使用同一个正则表达式的情况下，
# 应该将它进行编译以获得一个 pattern 对象，
# 然后直接调用这个 pattern 对象的方法。
compiledPattern = re.compile(pattern)
print compiledPattern
print dir(compiledPattern)
print compiledPattern.search('M')
