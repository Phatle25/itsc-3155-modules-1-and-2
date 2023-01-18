originalarray = []
for i in range(10):
    x = int(input("Enter number:" ))
    originalarray.append(x)

# remove duplicates
s = set()
for i in originalarray:
    # set will not accept duplicates
    s.add(i)
print("Original list:",originalarray)
# set will not accept duplicates
print("Nums that appear once: ",list(s)) 