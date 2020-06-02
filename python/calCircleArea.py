#!/usr/bin/python

# Asks for radis from circle and then outputs Circle Area

## Ideas for improvement ##
# - Check input type to ensure int is entered. 
# - Could also ask for input and check if radius or and adjust accordingly 
 
def calCircleArea(r):
	circleArea=3.14*r*r
	print("Area of the circle with radius", r, "is", circleArea)

radius=int(input("Please enter radius of circle: "))
calCircleArea(radius)
