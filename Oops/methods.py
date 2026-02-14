#Methods are functions that belong to objects.
class Student:
    college_name="ABC College"
    
    def __init__(self, name, marks):
        self.name = name # obj
        self.marks =marks
    
    def welcome(self):
        print("welcome student")

s1= Student("karan",97)
s1.welcome()