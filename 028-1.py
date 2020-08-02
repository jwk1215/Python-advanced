#! /usr/bin/env python

import sys

seq = sys.argv[1]

def comp(seq):
    d_comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp = ''
    for s in seq:
        comp += d_comp[s]
    return comp

c = comp(seq)
print(c)

#python 028-1.py ATGTTATAG



