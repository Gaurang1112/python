'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero. '''

a = int(input())
b = int(input())
c= int(input())
if a ==b or b == c or c  == a:
    sum= 0
    print(sum)
else:
    sum = a+b+c
    print(sum)
