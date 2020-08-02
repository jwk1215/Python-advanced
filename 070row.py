#! /usr/bin/env python

f = '070.vcf'

cnt = 0

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        cnt += 1

print(cnt)
 

