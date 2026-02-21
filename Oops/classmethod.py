# a class method is bound to the class and receives the class as an imolicit first argument.
class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     #Person.name = name
    #     self.__class__.name="Rahul kumar"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)