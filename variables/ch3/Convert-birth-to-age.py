# Use Python's built-in datetime module
from datetime import date
def age(birthdate):
    today = date.today()
    one_or_zero = ((today.month, today.day) < (birthdate.month, birthdate.day))

    year_difference = today.year - birthdate.year

    age = year_difference - one_or_zero
    return age
y=int(input('Enter year Birthday='))
m=int(input('Enter month Birthday='))
d=int(input('Enter day Birthday='))
print('Your age is : ',age(date(y,m,d)))
'''print(age(date(2000, 1, 1))) '''