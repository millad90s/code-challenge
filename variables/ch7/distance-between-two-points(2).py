import math
# I found the following function from the internet
def check_float(f_number):
    if all(c.isdigit() or c == '.' for c in f_number) and f_number.count('.') ==1:
        return True
    elif f_number.isnumeric():
        return True
    else:
        return False
    
# Get Coordinates of two points (x1, y1 , x2 , y2) from user  
x1 = input('The length of the first point (x1) = ')
y1 = input('The width of the first point (y1) = ')
x2 = input('The length of the seccond point (x2) = ')
y2 = input('The width of the seccond point (y2) = ')

# Check values to numeric values 
if check_float(x1) and check_float(y1) and check_float(x2) and check_float(y2):
    p = [float(x1), float(y1)] # Define two point from their Coordinates 
    q = [float(x2), float(y2)] # Define two point from their Coordinates 
    print(math.dist(p, q))     # Use the dist method to calculate the distance between two points and print them
else:
    print('You must insert integer value')