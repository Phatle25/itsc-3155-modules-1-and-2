# asking for user input for ROW & COLUMN where we need to insert 1
row = int(input("Enter a row number from 1 to 5: "))
columm = int(input("Enter a column number from 1 to 5: "))
# defining an array of 5,5 and initializing them with all 0
array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#initializing the array index with respective row & colum with 1    
array[row-1][columm-1] = 1
#for loop taking an entire row of that array
for a in array:
    # inner for loop to go through that row
    for i in a:
        #printing all the columns of that row
        print(i, end="")

    print()
