a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b:
    if a>c:
        print("A Is Greater")
    else:
        print("C Is Greater")
elif b>c:
    print("B Is Greater")
else:
    print("C Is Greater")
