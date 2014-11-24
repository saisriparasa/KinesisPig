set kinesis.endpoint.region us-west-2;
set kinesis.records.batchsize 30;
set kinesis.nodata.timeout 5;

A = load 'js-test' using com.amazon.emr.kinesis.pig.KinesisStreamLoader('kinesis.iteration.timeout=10') as (line:chararray);
Z = FOREACH A GENERATE FLATTEN(STRSPLIT(line, '\t')) as (f1:chararray, f2:chararray);
B = FOREACH Z GENERATE f2;
G = GROUP B BY $0;
C = FOREACH G GENERATE $0, COUNT($1);
         
set kinesis.checkpoint.enabled true;
set kinesis.checkpoint.metastore.table.name MyEMRKinesisTable;
set kinesis.checkpoint.metastore.hash.key.name HashKey;
set kinesis.checkpoint.metastore.range.key.name RangeKey;
set kinesis.checkpoint.logical.name TestLogicalName;
set kinesis.checkpoint.iteration.no $input;

STORE C into 's3://aws-sai-sriparasa/op/pig-kinesis/iteration_$input'; 
