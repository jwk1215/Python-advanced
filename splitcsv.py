#! /usr/bin/env python

#python으로 csv 파일과 tsv 파일을 읽어서 출력해봅시다
#각 라인을 csv 는 comma 구분자로
#tsv는 tab 구분자로 split 하여 나온 결과를 출력해봅시다

import sys

file_name = sys.argv[1]

def read_csv(file_name):
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

result = read_csv(file_name)
print(result)

#python splitcsv.py read_sample.csv

      
#18라인까지 하고 결과를 봤을 경우:
#[['1', 'ACAGGGTTA', 'Influenza'], ['2', 'TTAACCAAG', 'Herpes'], ['3', 'GCGAATGAC', 'Epstein-barr']]

#19라인을 추가하고 결과를 봤을 경우:
[{'#id': '1', 'sequence': 'ACAGGGTTA', 'species': 'Influenza'}, {'#id': '2', 'sequence': 'TTAACCAAG', 'species': 'Herpes'}, {'#id': '3', 'sequence': 'GCGAATGAC', 'species': 'Epstein-barr'}]



