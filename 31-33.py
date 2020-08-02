#! /usr/bin/env python


#문자열AA,AC,AG,AT 를 쉼표를 기준으로 리스트로 바꿔보세요
seq = 'AA,AC,AG,AT'

splitted = seq.split(',')
print(splitted)

#[“AA”, “AC”, “AG”, “AT”]에 문자열 “CA” 를 추가해보세요
add = splitted.append('CA')
print(splitted)

#169[“AA”, “AC”, “AG”, “AT”]의 순서를 뒤집어보세요

print(splitted[::-1])


