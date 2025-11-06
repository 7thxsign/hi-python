
class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #instance method
    def get_info(self):
        return f'Student {self.name} has GPA {self.gpa}'

    #class method
    @classmethod
    def get_count(cls):
        return f'The total count is: {cls.count}'

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'The average GPA is: {cls.total_gpa / cls.count:.2f}'

student1 = Student('John', 6.7)
print(student1.get_info())
print(Student.get_count(), end=' \n \n')

student2 = Student('Doe', 4.6)
print(student2.get_info())
print(Student.get_count(), end=' \n \n')

student3 = Student('Alexis', 6.9)
print(student3.get_info())
print(Student.get_count(), end=' \n \n')

print(Student.get_average_gpa())