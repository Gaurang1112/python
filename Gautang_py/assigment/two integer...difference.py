'''Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5. '''

a = int(input())
b = int(input())

plus = a+b
minus = a-b
if a==b or  plus== 5 or  minus ==5:
    print("True")
else:
    print("false")
