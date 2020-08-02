#! /usr/bin/env python

f = '059.fasta'

d = {}
with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        for s in line.strip():
            print(s)
            if s in d:
                d[s] += 1
            else:
                d[s] = 1


print(f"A의 개수: {d['A']}")
print(f"T의 개수: {d['T']}")
print(f"G의 개수: {d['G']}")
print(f"C의 개수: {d['C']}")



