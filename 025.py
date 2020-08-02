#! /usr/bin/env python

#문자열변수 Seq1 에 “ATGTTATAG” 가 담겨있습니다
#Seq1에서 3 칸씩 건너뛰며 출력 즉 첫 번째 네 번째 일곱 번째만 출력하는
#프로그램을 작성해보세요

Seq1 = "ATGTTATAG"

for i in range(0, len(Seq1), 3):
    #print(i)
    #print(Seq1[i])
    print(i, Seq1[i])






