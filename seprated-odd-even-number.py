# Take a list of numbers and separate the even
# and odd numbers and return the output as two separate lists,
# one for even numbers and one for odd numbers.
# The -l or --list op    tion is the desired option for this Python service.

import random

random_list = []
even_number = []
odd_number = []

count_number = int(input("How mane numbers do you need? "))
for i in range(count_number):
    random_list.append(random.randint(1, 10000))
for select in random_list:
    if select % 2 == 0:
        even_number.append(select)
    else:
        odd_number.append(select)

print("Random list: ", random_list)
print("Even Number: ", even_number)
print("Odd Number : ", odd_number)
