allnumbers = []
evennumbers = []
number = input("Enter a number or QUIT to quit: ")
while (number != "QUIT"):
    allnumbers.append(int(number))
    number = input("Enter a number or QUIT to quit: ")

for i in range(0, len(allnumbers)):
    if (allnumbers[i] % 2 == 0):
        evennumbers.append(allnumbers[i])
print("All Nums:", allnumbers)
print("Even Nums:", evennumbers)
