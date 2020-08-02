#! /usr/bin/env python

#변수 num1 에 들어있는 수가 3 의 배수인지 7 의 배수인지 판별해보세요.
#예시로 num1 에 21 을 넣어보겠습니다.


num1 = 21

#num1 = int(input("write num: "))



if num1 % 3 == 0 and num1 % 7 == 0:
    print("3과 7의 배수입니다.")
elif num1 & 3 == 0:
    print("3의 배수입니다.")
elif num1 % 7 == 0:
    print("7의 배수입니다.")
else:
    print("3의 배수도 아니고 7의 배수도 아닙니다.")



