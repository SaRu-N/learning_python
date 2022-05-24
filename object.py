# #object of class
from classes import Student
student1= Student("John ","Science",3.5,False)
student2= Student("Alice","Business",3.1,True)

print(student1.name)
print(student2.major)
print(student1.on_honor_roll())
print(student2.on_honor_roll())
