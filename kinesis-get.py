#! /usr/bin/python
import boto

kinesis = boto.connect_kinesis()
stream = kinesis.describe_stream('js-test')
shardId = stream['StreamDescription']['Shards'][0]['ShardId']
shardIterator = kinesis.get_shard_iterator('js-test',shardId,'TRIM_HORIZON')

while(True):
	recs = kinesis.get_records(shardIterator['ShardIterator'])
	shardIterator['ShardIterator'] = recs['NextShardIterator']
	print recs
