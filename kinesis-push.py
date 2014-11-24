#! /usr/bin/python
#import boto
import boto.kinesis as boto_kinesis
import datetime
import time

#kinesis = boto.connect_kinesis()
#streams = kinesis.list_streams()
#stream = kinesis.describe_stream('js-test')

kinesis = boto_kinesis.connect_to_region('us-west-2')

for i in xrange(1,100001):
	time.sleep(0.3)
	ct = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	
	#print 'The current time is \t'+ct	
	print kinesis.put_record('js-test','The current time is\t'+ct, ct)
