array1 = [] # initialize two lists
array2 = [] # initialize two lists

for i in range(5):
    # typecast the input value to int
    array1.append(int(input("Enter number of the first list: ")))

for i in range(5):
    # typecast the input value to int
    array2.append(int(input("Enter number of the second list: ")))

array3 = [] # create new list

for i in array1:
    if i in array2:
        array3.append(i)

print("First list:", array1)
print("Second list:", array2)
print("Common list:", array3)
