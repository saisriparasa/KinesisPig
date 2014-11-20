set kinesis.endpoint.region us-west-2;
set kinesis.records.batchsize 10000;
set kinesis.nodata.timeout 1;

A = load 'js-test' using com.amazon.emr.kinesis.pig.KinesisStreamLoader('kinesis.iteration.timeout=1') as (line:chararray);
dump A;
