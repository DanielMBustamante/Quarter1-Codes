#Program to Solve Area of Circle

#Import math library
import math

#declare variables
r = float(input("Enter the radius: "))
pi = math.pi
area = pi * r * r

#display output/result
print("The area of the circle is: {:.2f}".format(area))