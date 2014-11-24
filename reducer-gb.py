#! /usr/bin/python
#2014-11-23 22:31:20	1
#2014-11-23 22:31:20	1
#2014-11-23 22:31:20	1
import sys
import collections

d = {}

for i in sys.stdin:
	i = i.strip().split('\t')

	if i[0] in d.keys():
		d[i[0]] = d[i[0]] + 1
	else:
		d[i[0]] = 1

x = collections.OrderedDict(sorted(d.items()))

for i in x.items():
	print i
