#Exercise 1: Message
#Write a function called display_message() that prints one sentence telling everyone what you are 
#learning about in this chapter. Call the
#function, and make sure the message displays correctly.

def display_message():
    # Print a sentence
    print("I am learning about in this chapter.")

# Call the function
display_message()

#Exercise 2: Favorite Book
#Write a function called favorite_book() that accepts one parameter, title.
#The function should print a message, such as One of my favorite books is Alice in Wonderland. 
#Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    # This function takes a book title as an argument and prints a message
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Hunger Games")

#Exercise 3: T-Shirt
#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional
#arguments to make a shirt. Call the function a second time using keyword arguments.

# Define the function make_shirt
def make_shirt(size, message):
    # Print a sentence summarizing the size and message
    print(f"The shirt is {size} and has '{message}' printed on it.")

# Call the function using positional arguments
make_shirt("small", "LOVE THE WORLD")

# Call the function using keyword arguments
make_shirt(message="BATH SPA", size="Large")

#Exercise 4: Large Shirts
#Modify the make_shirt() function so that shirts are large by default with a message 
#that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'are you Smart?')

#Exercise 5: Cities
#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,
#such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

# Define a function called describe_city() that accepts the name of a city and its country
def describe_city(city, country="UAE"):
  # Print a simple sentence, such as Reykjavik is in Iceland
  print(city + " is in " + country)

# Call the function for three different cities, at least one of which is not in the default country
describe_city("Sharjah") # Sharjah is in UAE
describe_city("Dubai") # Dubai is in UAE
describe_city("London", "UK") # London is in UK


