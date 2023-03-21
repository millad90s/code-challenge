'''Gradebook: 
    Create a gradebook for a class using variables to store the students' grades 
    and calculate the average grade for the class.'''
# Function Average Number 
def avg_num(*num):
    return sum(num)/len(num)

""" Getting the number of names and the number of lessons  """
names_student = int(input('How many need do you names for student : '))
scores_student = int(input('How many need do you score for student : '))

student = {}  # for use dictionary for list
