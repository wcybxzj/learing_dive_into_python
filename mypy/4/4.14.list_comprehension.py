#!/usr/bin/env python
# -*- coding: utf-8 -*-

li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print [elem for elem in li if len(elem) > 1]
print [elem for elem in li if elem != "b"]
print [elem for elem in li if li.count(elem) == 1]
