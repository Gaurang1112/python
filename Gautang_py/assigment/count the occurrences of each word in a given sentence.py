'''Write a Python program to count the occurrences of each word in a
given sentence.'''

sentence=input("enter your sentence:")
word=input()
a = sentence.split(",")
count=0
for i in range(0,len(a)):
    if word == a[i]:
        count += 1
    else :
        pass
print(count)

