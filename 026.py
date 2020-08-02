#! /usr/bin/env python

#문자열 변수 Seq1 에 “ATGTTATAG” 가 담겨있습니다
#Seq1 에서 3 칸씩 건너뛰며 다음과 같이 출력해보세요
#ATG
#TTA
#TAG

Seq1 = "ATGTTATAG"

for i in range(0, len(Seq1), 3):
    print(i, i+3, Seq1[i:i+3])



