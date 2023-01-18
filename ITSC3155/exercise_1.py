# ask user to enter a string
userstring = input("Enter a string: ")
# declare string variable for lowercase and uppercase letter
uppercase = ""
lowercase = ""
# for loop to loop though each symbol i of the user input
for i in userstring:
    # if it is lowercase, then it will be saved in lower case
    if i.islower():
        lowercase = lowercase + i
    # if it is uppercase, then it will be saved in upper case
    elif i.isupper():
        uppercase = uppercase + i
    
# print out the lowercase letter first, then uppercase lettter
print(lowercase + uppercase)
