#! /usr/bin/env python

#문자열변수 Seq1 에 “AGTTTATAG” 가 담겨있습니다
#Seq1에서 TT 가 출현하는 index 를 출력해보세요

#TTT가 붙어있음을 주의합시다

#2
#3

import sys

seq1 = sys.argv[1]

for i in range(0, len(seq1), 1):
    if seq1[i:i+2] == 'TT':
        print(i, seq1[i:i+2])

#python 030.py AGTTTATAG







