#! /usr/bin/env python

#문자열변수 Seq1 에 “ATGTTATAG” 가 담겨있습니다
#Seq1에서 A 는 T 로 T 는 A 로 C 는 G 로 G 는 C 로 바꾸어 출력해보세요


import sys

seq = sys.argv[1]

def comp(self):
    comp = ''
    for s in seq:
        if s == 'A':
            comp += 'T'
        elif s == 'T':
            comp += 'A'
        elif s == 'G':
            comp += 'C'
        elif s == 'C':
            comp += 'G'
    return comp

change = comp(seq)
print(change)


#python 028.py ATGTTATAG




