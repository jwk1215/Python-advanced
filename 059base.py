#! /usr/bin/env python

f = "059.fasta"

A = 0
C = 0
G = 0
T = 0

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            line.strip().split('\n')
        else:
            seq = line.strip()
            A += seq.count('A')
            C += seq.count('C')
            G += seq.count('G')
            T += seq.count('T')

print(f'A: {A}')   
print(f'C: {C}')
print(f'G: {G}')
print(f'T: {T}')                       
    
                




