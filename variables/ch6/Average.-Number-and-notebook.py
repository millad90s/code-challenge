'''Gradebook: 
    Create a gradebook for a class using variables to store the students' grades 
    and calculate the average grade for the class.'''
import pprint
# Function Average Number 
def avreage_num(num_list:list):
    return sum(num_list)/len(num_list)

""" Getting the number of names and the number of lessons  """
names_student = int(input('How many need do you names for student : '))
scores_student = int(input('How many need do you score for student : '))

student = {}  # for use dictionary for list

""" Running two nested loops to get its names, lessons and grades  """
for i in range(names_student):
    name_student=input('Insert student name: ')
    student.setdefault(name_student,{})

    for j in range(scores_student):
        lesson_score = input('Lesson name: ')
        student[name_student].setdefault(lesson_score,0)
        student[name_student][lesson_score]=int(input('What a score? '))

pprint.pprint(student)

    
