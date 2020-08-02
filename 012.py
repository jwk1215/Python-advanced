#! /usr/bin/env python

#앞의 5! 을 계산하여 반환하는 프로그램을 수정하여 
#함수에 값을 전달하여 반환하는 프로그램을 작성해보세요.
#예를들어 3 을 넣으면 3! 인 6 이 반환되게 작성합니다.


def factorial(num):
    result =1
    while num > 0:
        result *= num
        num -= 1
    return result

result = factorial(3)

print(result)
