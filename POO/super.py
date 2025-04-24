class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def greet (self):
        print("Hello! I'm a person.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        super().greet()
        print(f"Hi! i'm a student and my id is .{self.student_id}")

student = Student("John", 20, "S12345")
student.greet()

