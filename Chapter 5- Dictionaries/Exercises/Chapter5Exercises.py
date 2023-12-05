#Exercise 1: Person
#Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person = {
    'first_name': 'John',
    'last_name': 'Purisima',
    'age': 13,
    'city': 'Angat'
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

#Exercise 2: Glossary
#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
#their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between
#each word-meaning pair in your output.    

glossary = {
    'List': 'A collection of items in a particular order. Lists are mutable, meaning they can be modified after they are created.',
    'Tuple': 'An immutable list. Once a tuple is defined, its values cannot be changed.',
    'Dictionary': 'A collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.',
    'Loop': 'A structure for executing a block of code repeatedly.',
    'Function': 'A named block of code that performs a specific task. Functions allow you to write code once and use it multiple times.'
}
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

#Exercise 3: Glossary 2
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable list.',
    'set': 'A collection of unique items.',
    'function': 'A named block of code that performs a specific task.',
    'module': 'A file containing Python definitions and statements.',
    'loop': 'A way to iterate over a collection of items.',
    'string': 'A sequence of characters.',
    'integer': 'A whole number.',
    'float': 'A number with a decimal point.',
    'boolean': 'A value that is either True or False.'
}
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

#Exercise 4: Rivers
#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Han': 'South Korea'}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

#Exercise 5: Pets 
#Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, 
# loop through your list and as you do, print everything you know about
#each pet
pets = []
pet = {
    'animal type': 'cat',
    'name': 'mingming',
    'owner': 'john',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'tandang',
    'owner': 'jayric',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'oppa',
    'owner': 'Rafael',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

