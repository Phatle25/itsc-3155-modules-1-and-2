# ask user to put enter the a string
userinput = input("Enter a string: ")
# store the value of last index number of string character
# in variable i which is 1 less than length of string
i = len(userinput)-1
# while loop run until the value of i is less than 0
while (i >= 0):
    # print the string character from last index to first index number
    print(userinput[i])
    # decrement the value of variable i by 1
    i = i-1

