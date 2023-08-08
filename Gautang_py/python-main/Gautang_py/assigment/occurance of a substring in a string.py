#Write a Python program to count occurrences of a substring in a string.

str = input()

def function(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(dict)
function(str)
     
