#! /usr/bin/env python

f = '070.vcf'

cnt = 0

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        l_list = line.split('\t')
        #print(l_list)   
        if l_list[6] == 'PASS':
            cnt += 1

print(cnt)

