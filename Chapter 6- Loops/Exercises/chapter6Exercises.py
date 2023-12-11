#Exercise 1: Pizza Toppings
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.

while True:
    topping = input("Enter a pizza topping (or 'quit'): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza!")


#Exercise 2: Movie Tickets: :ballot_box_with_check:
#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, 
#the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, 
#the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket

while True:
    age = input("What is your age? ")
    if age == "quit":
        break
    elif int(age) < 5:
        print("Your ticket is free.")
    elif int(age) <= 12:
        print("Your ticket costs $20.")
    else:
        print("Your ticket costs $30.")

#Exercise 3: Infinity 
#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

#while True:
# print("HI I'M RAFAEL!")


#Exercise 4: Deli
#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['tuna', 'grilled cheese', 'ham cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

   
#Exercise 5: No Pastrami 
#sing the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['beef', 'pastrami', 'cheese', 'ham', 'pastrami', 'pastrami', 'chicken']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")

finished_sandwiches.append(sandwich)

print("\nHere are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")




























