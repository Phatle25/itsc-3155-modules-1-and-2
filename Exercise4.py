# asking user to enter input
print("Enter the number of floats you want to enter")
# taking the number of floats as input
number = int(input())
# create a list to store the input
array = []
# use for loop to take input of n elements
for i in range(number):
    # appends the next input value given by the user to the list
    array.append(int(input()))
# declare mean variable
average = 0
# for loop to calculate the mean of all the value in the array
for i in array:
    average += i
average /= number

print("List: ")
# print out the list
for i in array:  # print the list
    print(i, end=" ")
print()

print("Average: " + str(average))  # prints mean
