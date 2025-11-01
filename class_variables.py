class Student:

    class_year = 2023
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student('John', 25)
print(Student.num_students)
student2 = Student('Doe', 30)
print(Student.num_students)
student3 = Student('Pork', 32)
print(Student.num_students)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.class_year) #recommended way of using class variables