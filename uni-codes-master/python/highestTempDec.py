#!/usr/bin/python 

# Calculates the highest temperature for the month of Dec

# Could check user input and ensure that integers are entered.
# Could also seperate into different modules or classes.

highestTemp = 0
decDays = 31
for d in range(decDays):
	print("\nCurrent day is: ", d+1)
	temp=int(input("Enter a temperature for today: \n"))
	if (temp > highestTemp):
		highestTemp = temp
		print("Current highest temp is ", highestTemp)
print("We have reached the end of the month!")
print("The highest temp for the month was:", highestTemp)