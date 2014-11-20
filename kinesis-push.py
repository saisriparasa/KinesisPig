#! /usr/bin/python
import boto
import datetime
import time

kinesis = boto.connect_kinesis()
#streams = kinesis.list_streams()
#stream = kinesis.describe_stream('js-test')

for i in xrange(1,100001):
	time.sleep(0.3)
	ct = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	
	print kinesis.put_record('js-test','The current time is\t'+ct, ct)
