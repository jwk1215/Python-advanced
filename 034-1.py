#! /usr/bin/env python

#리스트[ 1, 1, 2, 0, 0, 2, 3, 3] 에서 각 요소의 출현 빈도를
#사전으로세어보세요
#{0: 2, 1: 2, 2: 2, 3: 3}


l = [1, 2, 3, 0, 0, 2, 3, 3]

d = {}

for elem in l:
    if elem in d:
        d[elem] +=1
    else:
        d[elem] = 1

print(d)






