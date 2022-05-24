from unicodedata import name


class Student:
    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major =major
        self.gpa=gpa
        self.is_on_probation=is_on_probation
    # Object function 
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
class Question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer

class Chef:
    def make_momos(self):
        print("The chef can make momos")
    def make_salad(self):
        print("The chef can make a salad")
    def make_special_dish(self):
        print("The chef can make chatpate")

# inheritance
class ChineaseChef (Chef):
    def make_special_dish(self):
        print("The Chef can make Sushi")
    def make_fried_rice(self):
        print("The Chef can make fried rice")