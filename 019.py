#! /usr/bin/env python

#다음 스크립트는 파일이 없다는 오류가 발생합니다
#오류가발생하지 않도록 try except 를 사용해보세요

#with open('noname.txt', 'r') as fr:
#    read = fr.readlines()

#print(read)



try:
    with open("noname.txt", "r") as fr:
        read = fr.readlines()
    print(read)

except FileNotFoundError:
    print("파일이 없습니다")

    


