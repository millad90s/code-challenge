''' Distance Calculator: 
Write a program that prompts the user for two points on a plane 
and calculates the distance between them using variables to store the values.
'''
import math

# Get Coordinates of two points (x1, y1 , x2 , y2) from user  
x1 = float(input('The length of the first point (x1) = '))
y1 = float(input('The width of the first point (y1) = '))
x2 = float(input('The length of the seccond point (x2) = '))
y2 = float(input('The width of the seccond point (y2) = '))

# Define two point from their Coordinates 
p = [x1, y1]
q = [x2, y2]

# Use the dist method to calculate the distance between two points and print them
print(math.dist(p, q))

