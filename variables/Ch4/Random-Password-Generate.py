'''Password Generator: Create a program that generates a random password for the user using variables to store the password.'''
import random
# Define valid char
symbol = "!@#$%^&*()_+"
number = "1234567890"
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define valid Number char = 8(1+2+5)
num_symbol = 1
num_number = 2
num_letter = 5

password=""
# Generate 1 symbol for password
for n in range(num_symbol):
    password+=random.choice(symbol)
# Generate 2 number for password
for n in range(num_number):
    password+=random.choice(number)
# Generate 5 letter for password
for n in range(num_letter):
    password+=random.choice(letter)










