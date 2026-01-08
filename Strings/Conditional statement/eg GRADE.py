marks=float(input("enter your marks:"))

if(marks>=90):
    Grade= "A"
elif(marks>=80 and marks<90):
     Grade= "B"
elif(marks>=70 and marks<80):
     Grade= "B"
elif(marks>=60 and marks<70):
     Grade= "D"
else:
     Grade= "E"
print("Grade of Student:",Grade)
