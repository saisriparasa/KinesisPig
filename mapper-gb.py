#! /usr/bin/python
import sys

for i in sys.stdin:
	print (i.strip().split('\t'))[1]+'\t'+str(1)
