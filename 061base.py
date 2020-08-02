#! /usr/bin/env python

f = '061.fastq'

n = 0
length = 0

with open(f, 'r') as fr:
    for line in fr:
        if n % 4 == 1: #n = 1
            length += len(line.strip())
        n +=1

print(length)


            



