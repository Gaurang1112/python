file=open("tops1.txt","w")
file.write("this is file input/output demo using python.")
file.close
print("file written successfully")

print("*"*60)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*60)

file=open("tops1.txt","a")
file.write("this file is appended./n")
file.close


file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*60)

print("*"*60)

file=open("tops2.txt","w+")
file.write("tops is read/write operation using python.")
file.seek(0)
file.close

