rno=int(input("Enter Roll No:"))
sname=input("Enter Student Name:")
s1=int(input("Enter Marks Of Subject 1:"))
s2=int(input("Enter Marks Of Subject 2:"))
s3=int(input("Enter Marks Of Subject 3:"))

Total=s1+s2+s3
per=Total/3

print("Student Roll No:",rno)
print("Student Name:",sname)
print("Total:",Total)
print("Percentage",per)

if per>=70:
    print("Distiction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass")
else:
    print("Fail")        
