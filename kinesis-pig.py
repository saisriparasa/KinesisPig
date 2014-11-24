#! /usr/bin/python
import subprocess

for i in xrange(1,11):
	print "en sub process"
	subprocess.call(('pig -f /home/hadoop/kinesis.pig -param input='+str(i)).split(), shell=False)
	print "out sub process"
