''' Distance Calculator: 
Write a program that prompts the user for two points on a plane 
and calculates the distance between them using variables to store the values.
'''
import math

# Get Coordinates of two points (x1, y1 , x2 , y2) from user  
x1 = input('The length of the first point (x1) = ')
y1 = input('The width of the first point (y1) = ')
x2 = input('The length of the seccond point (x2) = ')
y2 = input('The width of the seccond point (y2) = ')

# Check values to numeric values 
if x1.isnumeric() and y1.isnumeric() and x2.isnumeric() and y2.isnumeric():
    p = [float(x1), float(y1)] # Define two point from their Coordinates 
    q = [float(x2), float(y2)] # Define two point from their Coordinates 
    print(math.dist(p, q))     # Use the dist method to calculate the distance between two points and print them
else:
    print('You must insert integer value')



