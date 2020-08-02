#! /usr/bin/env python

#mySum이라는 이름의 함수를 만든 후 이 함수에 (2, 3), (5, 7), (10,15)
#함수의 값으로 전달하여 전달한 두 수를 더하여 출력하는 프로그램을 작성해보세요.


#1
def mySum(a, b):
    return a+b

result1= mySum(2,3)
print(result1)
result2 = mySum(5,7)
print(result2)
result3 = mySum(10,15)
print(result3)


#2
def mySum(a,b):
    print("%s + %s = %s" %(a, b, a+b))

def mySum(a,b):
    print("{0}+{1}={2}".format(a, b, a+b))

mySum(2, 3)
mySum(5, 7)
mySum(10, 15)

#3
def mySum(a,b):
    print(f"{a}+{b} = {a+b}")

mySum(2, 3)
mySum(5, 7)
mySum(10, 15)


