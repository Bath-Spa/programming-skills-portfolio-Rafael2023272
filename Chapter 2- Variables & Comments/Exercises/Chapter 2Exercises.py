#EXERCISE 1 VARIABLES
#Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.

A = "Hello, My name is Rafael Purisima"
print(A)
A = "Hello, How are you?"
print(A)


#EXERCISE 2 VARIABLES
#Find a quote from a famous person you admire. Print the quote and the name of its author.

A="Albert Einstein"
B="once said,"
C='"You never fail until you stop trying"'

print(A,""+ B,""+C,)


#EXERCISE 3 STRIPPING NAMES

W="\trafael purisima\n"
print(W)
print(W.lstrip())
print(W.rstrip())
print(W.strip())


#EXERCISE 4 FAVORITE NUMBER

M=123
M=(input("Enter your favorite number = "))
print("My favorite number is = {0}" .format(M))


#EXERCISE 5 USB CHOPPER

usb_bought=("total usb bought are=")
money_left=("total money that is left=")
print(usb_bought+str(int(50/6)))
print(money_left+str(50%6))

