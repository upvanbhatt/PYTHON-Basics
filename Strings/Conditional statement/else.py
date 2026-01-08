#else: it is written only once and only in the last 
#when all above statement get False then only else get executed
light= input("enter light color:")
if(light=="red"):
    print("Stop")
elif(light=="green"):#not Green case sensitive
    print("go")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken")

print("end of code")

#if else
age=int(input("enter your age:"))

if(age>=18): #or True
    print("can vote and apply for licence")
    print("can drive")
else:
    print("cannot vote")
