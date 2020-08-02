#! /usr/bin/env python

#python으로 txt 파일을 읽어서 출력해봅시다.

#read_sample.txt파일을 만들어준다
# >leader
# ACGTACGTAAA
# TTTAAAGGAAA

#read_sample.txt파일을 열어서 읽고 해당 내용을 출력한다.


import sys

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

f = 'read_sample.txt'

def readtxt(f):
    ret = ''
    with open(f, 'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            ret += line.strip()  #두 줄로 나누어져있는 염기서열이 한줄로 합쳐짐
    return ret

f = sys.argv[1]
txt =readtxt(f)
print(txt)

#python readtxt.py read_sample.txt



