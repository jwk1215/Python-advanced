#! /usr/bin/env python

f = '070.vcf'

with open(f, 'r') as handle:
    for line in handle:    
        if line.startswith('##'):
            continue
        if line.startswith('#'):
            header = line.strip().split('\t')
            #print(header)
            id_idx = header.index("ID")
            #print(id_idx)
            continue

        splitted = line.strip().split('\t')
        #print(splitted)            
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != ".":
            print(f'{chrom}-{pos}-{ref}-{alt}-{id_}')



            
