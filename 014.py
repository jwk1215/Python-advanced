#! /usr/bin/env python


#사용자로부터 한 글자를 입력받아 입력받은 문자가
#숫자인지문자인지 출력하는 프로그램을 작성해보세요.

#1
import sys

INput = sys.argv[1]

if INput.isalpha():
    print("문자입니다.")
elif INput.isnumeric():
    print("숫자입니다.")
else:
    print("숫자도 문자도 아닙니다.")

#2

INput = input("Enter: ")

if INput.isalpha():
    print("문자입니다.")
elif INput.isnumeric():
    print("숫자입니다.")
else:
    print("숫자도 문자도 아닙니다.")




