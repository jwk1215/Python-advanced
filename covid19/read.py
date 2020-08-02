#! /usr/bin/env python

f = "read_sample.txt"

with (f, 'r') as fread:
    for line in fread:
        print(line.strip())



