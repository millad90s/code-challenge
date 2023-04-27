# Take a list of numbers and separate the even
# and odd numbers and return the output as two separate lists,
# one for even numbers and one for odd numbers.
# The -l or --list option is the desired option for this Python service.

import argparse

# Parameters receive

params = argparse.ArgumentParser(description='number derivation for even and odd')
params.add_argument('--list', '-l', nargs='+', type=int)
arguments = params.parse_args()

# Define list for even and odd
even_number = []
odd_number = []

if arguments.list is not None:
    for number in arguments.list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            odd_number.append(number)

print("Even Number: ", even_number)
print("Odd Number : ", odd_number)
