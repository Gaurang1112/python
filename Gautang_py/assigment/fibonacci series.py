#Write a Python program to get the Fibonacci series of given range.

n=int(input("Enter Number"))

n1=0
n2=1
count=0

if n<=0:
      print("Enter a Positive Number")
elif n==1:
      print("Enter a upto 1")
else:
      print("Fibonacci Series")

while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1
        #nth=n1+n2
      
