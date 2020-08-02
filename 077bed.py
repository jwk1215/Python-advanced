#! /usr/bin/env python

f = '077.bed'

length = 0

with open(f, 'r') as handle:
    for line in handle:
        chrom_start_end = line.split('\t')
        #print(chrom_start_end)
        chrom = chrom_start_end[0]
        start = int(chrom_start_end[1])
        end = int(chrom_start_end[2])
        #print(start)
        #print(end)
        length += end -start

print(length)
