#Exercise 1: Print strings
#Write a Python program to print the following string in a specific format

#Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. 
#Twinkle, twinkle, little star, How I wonder what you are

print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.")
print("Twinkle, twinkle, little star, How I wonder what you are")


#Exercise 2: Write a Python program to get the Python version you are using.
import sys
print(sys.version)

import platform
print(platform.python_version())


#Exercise 3: Print Date and Time
#Write a Python program to display the current date and time.
date="October 21, 2023"
print(date)

time="2:15 pm"
print(time)


#Exercise 4: Strings Concatination
#Write three strings in different variables and print the output as one string. 
R="rafael"
S="sicat"
P="purisima"

print (R,"" + S,"" + P)


#Exercise 5: Compute area of Circle
#Write a Python program which accepts the radius of a circle from the user and compute the area.
PI = 3.14
radius = float(input("Enter the radius of a circle: "))
area = PI * radius * radius
print("The area of the circle with radius", radius, "is:", area)

