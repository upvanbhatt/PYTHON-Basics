class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print("hello")

    

s1=Student("tony stark", [99,98,97])

s1.hello()