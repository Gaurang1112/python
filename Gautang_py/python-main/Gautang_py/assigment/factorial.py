#Write 
#Python program to get the Factorial number of given number.

a=int(input("Enter Factorial"))

fac=1

if a<0:
    print("we can't find negative number")

elif a==0:
    print(" 0")

else:
    for i in range(1,a+1):
        fac= fac*i
    print(fac)


        
