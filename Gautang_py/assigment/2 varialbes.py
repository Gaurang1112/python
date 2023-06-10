#Write python program that swap two number with temp variable and
# without temp variable.

x=int(input("Enter value of X"))
y=int(input("Enter value of Y"))

temp=x
x=y
y=temp
print("The value of x afer swapping:{}".format(x))
print("The value of y afer swapping:{}".format(y))
