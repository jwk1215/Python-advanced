#! /usr/bin/env python

f = '061.fastq'

cnt1=0
cnt=0
with open(f, 'r') as handle:
    for line in handle:
        header = line.strip()
        if cnt % 4 == 0:
            #print('header', line)
            cnt1+=1
        elif cnt % 4 == 1: # cnt =1
            three = line.strip()
            #print('$$$$$', three)
        elif cnt % 4 == 2: # cnt =2
            two = line.strip()
            #print('****', two)
        elif cnt % 4 == 3: # cnt =3
            one = line.strip()
            #print('#####', one)
        cnt += 1
            
print('총라인수=',cnt)
print('read수 =',cnt1)
