#! /usr/bin/env python

#다음 스크립트는 여러 오류가 있습니다
#값을 0 을 넣는경우, 값을 넣지 않는 경우
#두 가지 오류가 발생하는 상황을 처리해 봅시다

#num = int(input('Enter: '))
#print(10/num)

try: 
    num = int(input('Enter: '))
    print(10/num)

except ZeroDivisionError:
    print("0이상의 값을 넣어주세요.")

except ValueError:
    print("값을 넣어주세요.")




