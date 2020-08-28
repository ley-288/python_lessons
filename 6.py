#modules and pip

import useful_tools #name of local external file

print(useful_tools.roll_dice(10))#function from file


..

#classes and objects

class Student: #class. overview. template

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name #name of student is going to be equal to value we pass in. self refers to object
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


from Student import Student #actual information

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student2.name)


..


#Multiple choice test

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions: #for each question in the questions array
        answer = input(question.prompt) 
        if answer == question.answer: #if user answer is equal to answer of question we're asking
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


..

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())


..



go to 7.py





