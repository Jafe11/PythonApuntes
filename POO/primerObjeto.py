class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def greet(self):
        print(f"Hi, my name is: {self.name} and i'm {self.age} years old")

persona1 = Person("Juan", 25)	

persona1.greet()