'''Write a Python function that takes a list of words and returns the length
of the longest one.'''

def longest(a):
    max1=len(a[0])
    temp=[0]
    for i in a:
        if len(i)>max1:
            max=len(i)
            temp=i
    print("the longest number is:",temp)
    print("the lenth of this word is:",max1)
