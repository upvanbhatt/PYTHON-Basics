class Student:
    # self parameter is a reference to the current instance of the class and is used to access variables that belong to the class. 
    #self can also be written as abcd or xyz it will do the same work 
    def __init__(self, fullname): # self is first parameter
        self.name = fullname
        print("adding new student in database..")

s1=Student("karan")
print(s1.name) #karan

s2=Student("arjun")
print(s2.name)#arjun