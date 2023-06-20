#function with no argument & no return value

def printline():
    print("*"*50)
printline()
print("welcome to tops")
printline()

#function with no argument & no return value

def add(a,b):
    print("Addition:",a+b)

printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
add(x,y)
printline()

#function with no argument & no return value

def sub(a,b):
    return a-b
printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
ans=sub(x,y)
print("substractuion:",ans)
printline()
