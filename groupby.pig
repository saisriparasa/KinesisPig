A = LOAD 's3://aws-sai-sriparasa/op' USING PigStorage('\t') AS (f1:chararray, f2:chararray);
B = FOREACH A GENERATE f2;
G = GROUP B BY $0;
C = FOREACH G GENERATE $0, COUNT($1);

DUMP C;
