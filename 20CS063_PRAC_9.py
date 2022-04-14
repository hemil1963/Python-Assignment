''' ID:-20CS063    NAME:Hemil Patoliya'''
'''Aim:-Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.
 The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by 
 inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result 
 from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this 
 relationship.'''

class Student:

    rollNumber = None

    name = None

class Exam(Student):

    marks = []

class Result(Exam):

    def print_total(self):

        print(sum(self.marks))

r = Result()

print("\nPREPARED BY-20CS063\n")

r.name = (input("Enter name of student : "))

r.rollNumber = int(input("Enter roll number of student : "))

for i in range(1, 7):

    r.marks.append(int(input("Enter marks of "+str(i) + " subject : ")))

print("Total marks : ")

r.print_total()
