#EXERCISE 1
#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

names = ["John", "Jacob", "Rafael"]

print(names[0])
print(names[1])
print(names[2])


#EXERCISE 2
#Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be
#personalized with the person’s name.

names = ['John', 'Jacob', 'Rafael']

msg = f"Hello! How are you, {names[0].title()}!"
print(msg)
msg = f"Hello! How are you, {names[1].title()}!"
print(msg)
msg = f"Hello! How are you, {names[2].title()}!"
print(msg)


#EXERCISE 3
#Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

favorite_transportation = ["train", "airplane","yatch"]

print("I would like to own a {}".format(favorite_transportation[0]))
print("I would like to own a {}".format(favorite_transportation[1]))
print("I would like to own a {}".format(favorite_transportation[2]))

#EXERCISE 4
#If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d
#like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

Guest_list = ["Queen Elizabet", "Elon Musk", "Bill Gates"]

print("You are invited to my dinner tommorow night at 7pm {}".format(Guest_list[0]))
print("You are invited to my dinner tommorow night at 7pm {}".format(Guest_list[1]))
print("You are invited to my dinner tommorow night at 7pm {}".format(Guest_list[2]))

#EXERCISE 5
#You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.

guests = ['Queen Elizabet', 'Elon Musk', 'Bill Gates']
name = guests[0].title()
print(f"{name}, Hi! please come to my dinner tomorrow at 7pm.")
name = guests[1].title()
print(f"{name}, Hi! please come to my dinner tomorrow at 7pm.")
name = guests[2].title()
print(f"{name}, Hi! please come to my dinner tommorow at 7pm.")
name = guests[2].title()
print(f"\nSorry,{name},I can't make it to your dinner.")

# Bill Gates can't make it! Let's invite Taylor swift instead.
del(guests[2])
guests.insert(2, 'Taylor Swift')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to my dinner tommorow at 7pm.")
name = guests[1].title()
print(f"{name}, please come to my dinner tommorow at 7pm.")
name = guests[2].title()
print(f"{name}, please come to my dinner tommorow at 7pm.")

#EXERCISE 6: Shrinking Guest List 
#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
#print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty 
#list at the end of your program.    

guests = ["Queen Elizabet", "Elon Musk", "Taylor Swift"]
print("Original guest list: ", guests)

print("\nSorry, we can only invite two people for dinner.")
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"Sorry {popped_guest}, we can't invite you to dinner.")

print(f"\n{guests[0]} and {guests[1]}, HI! you're still invited to dinner!")

del guests[0]
del guests[0]
print("\nFinal guest list: ", guests)

#EXERCISE 7: Seeing the World 
#Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse() to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
places = ['Seoul', 'London', 'New York', 'Paris', 'Antartica']
print("Original order:")
print(places)
print("\nAlphabetical order:")
print(sorted(places))
print("\nOriginal order:")
print(places)
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))
print("\nOriginal order:")
print(places)
places.reverse()
print("\nReversed order:")
print(places)
places.reverse()
print("\nOriginal order:")
print(places)
places.sort()
print("\nAlphabetical order:")
print(places)
places.sort(reverse=True)
print("\nReverse alphabetical order:")
print(places)