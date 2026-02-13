#constructor:- All classes have a function called __init__(), which is always executed when 
# the object is being initiated.
class Student:
    name="karan"
    def __init__(self): # self is first parameter
        print(self)
        print("adding new student in database..")

s1=Student()
print(s1) #s1 and self have same location

