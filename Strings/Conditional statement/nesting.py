#nesting: if inside an if
age=int(input("enter your age:"))

if(age>=18): #or True
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")