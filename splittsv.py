#! /usr/bin/env python

#python으로 csv 파일과 tsv 파일을 읽어서 출력해봅시다
#각 라인을 csv 는 comma 구분자로
#tsv는 tab 구분자로 split 하여 나온 결과를 출력해봅시다

import sys

file_name = sys.argv[1]

def read_tsv(file_name):
    ret = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(',')
                continue
            splitted = line.strip().split(',') 
            d = dict(zip(header, splitted)) 
            ret.append(d)
        return ret

result = read_tsv(file_name)
print(result)

#python splittsv.py read_sample.tsv



#결과
"""
[{'#id\t|sequence\t|species': '1\t|ACAGGGTTA\t|Influenza'}, {'#id\t|sequence\t|species': '2\t|TTAACCAAG\t|Herpes'}, {'#id\t|sequence\t|species': '3\t|GCGAATGAC\t|Epstein-barr'}]
"""




