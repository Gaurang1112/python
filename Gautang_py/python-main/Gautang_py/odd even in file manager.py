import random

data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")
data.close()
even.close()
odd.close()

print("data file content")
data=open("data.txt","r")
print(data.read())
data.close()

print("even file content")
even=open("even.txt","r")
print(even.read())
even.close()

print("odd file content")
odd=open("odd.txt","r")
print(odd.read())
odd.close()
