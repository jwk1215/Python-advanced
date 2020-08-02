#! /usr/bin/env python

#read_sample.txt 파일을 읽어 내용을 출력해보세요

#1
f = open('read_sample.txt', 'r')
r = f.readlines()
f.close()

for s in r:
    print(s.strip())


#2
f = 'read_sample.txt'

with open(f, 'r') as handle:
    for i in handle:
        print(i.strip())



