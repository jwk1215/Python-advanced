#! /usr/bin/env python

#5!을 계산하여 반환하는 프로그램을 작성해보세요
def factorial():
    num =5
    result =1
    while num > 0:
        result *= num
        num -= 1
    return result

result = factorial()

print(result)


