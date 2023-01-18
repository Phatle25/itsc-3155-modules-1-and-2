# ask user to put in a number greater than 1
number = int(input("Enter input greater than 1: "))
# for loop to iterated from 0 to number+1 
for i in range(0, number+1):
    # print out the respective cubes of i 
    print("The cube of", i, "is:", i**3)
