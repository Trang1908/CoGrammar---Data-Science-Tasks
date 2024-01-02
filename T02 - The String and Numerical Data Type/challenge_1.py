# Ask the user to enter the lengths of all three sides of a triangle
side1 = int(input("Please enter the first side length of a triangle: "))
side2 = int(input("Please enter the second side length of a triangle: "))
side3 = int(input("Please enter the third side length of a triangle: "))
print()

# Calculate the semi-perimeter of the triangle
s = (side1 + side2 + side3) / 2
print()

# Calculate the area of the triangle
import math
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
# Print out the area
print(area)