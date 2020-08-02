#! /usr/bin/env python

f = 'read_sample.tsv'

def read_csv(f):
    ret = []
    with open(f,'r') as handle:
        ret = []
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split('\t')
                continue
            splitted = line.strip().split('\t')
            d = dict(zip(header, splitted))
            ret.append(d)
        return ret

ret = read_csv(f)
print(ret)
                


