#Exercise 1: Alien Colors

alien_color='green'

#Write an if statement to test whether the alien’s color is green.
if alien_color=='green':

#print a message that the player just earned 5 points.
 print("You have earned 5 points.")

#Fails the if test
alien_color = 'red'

if alien_color == 'green':
 print("You just earned 5 points.")


#Exercise 2: Alien Colors #2
#If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

alien_color='green'

if alien_color=='green':
 print('You just earned 5 Points for shooting the Alien')

#If the alien’s color isn’t green, print a statement that the player just earned 10 points.

alien_color='green'
if alien_color=='blue':
 print('You just earned 10 points')

#Write one version of this program that runs the if block and another that runs the else block.

alien_color='red'
if alien_color=='red':
 print('Victory')
else: alien_color='blue'
print('Defeat')


#Exercise 3: Alien Colors #3

#If the alien is green, print a message that the player earned 5 points.

alien_color='green'
if alien_color=='green':
 print('You earned 5 points')

#If the alien is yellow, print a message that the player earned 10 points.

alien_color='yellow'
if alien_color=='yellow':
 print('You earned 10 points')

#If the alien is red, print a message that the player earned 15 points.

alien_color='red'
if alien_color=='red':
 print('You earned 15 points')

#Write three versions of this program, making sure each message is printed for the appropriate color alien.
#1

alien_color='black'
if alien_color=='black':
 print('You earned 5 points')


#2
alien_color='orange'
if alien_color=='gold':
 print('You earned 5 points')
elif alien_color=='orange':
 print('You earned 10 points')


#3
alien_color='violet'
if alien_color=='gold':
 print('You earned 5 points')
elif alien_color=='orange':
 print('You earned 10 points')
else: alien_color='violet'
print('You earned 15 points')


#Exercise 4: Stages of Life
#Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
#•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#•If the person is age 65 or older, print a message that the person is an elder.

age = 2 
if age==2:
    print("A baby")

age = 4
if age==2:
    print("A baby")
elif age==4:
    print("A toddler")

age = 13 
if age==2:
    print("A baby")
elif age==4:
    print("A toddler")
elif age == 13:
 print("A kid")

age = 20
if age==2:
    print("A baby")
elif age==4:
    print("A toddler")
elif age == 13:
    print("A kid")
elif age == 20:
    print("Teenager")


age = 65
if age==2:
    print("A baby")
elif age==4:
    print("A toddler")
elif age==13:
    print("A kid")
elif age==20:
    print("Teenager")
elif age==65:
    print("An adult")

age = 70
if age==2:
    print("A baby")
elif age==4:
    print("A toddler")
elif age==13:
    print("A kid")
elif age==20:
    print("Teenager")
elif age==65:
    print("An adult")
else:age=70
print("An elder")


#Exercise 5: Favorite Fruit

favorite_fruits ='apple', 'orange', 'pineapple', 'mango'

if 'banana' in favorite_fruits:
    print("You really like banana!")
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapple!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberry!")
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'mango' in favorite_fruits:
   print("You really like mango!")












