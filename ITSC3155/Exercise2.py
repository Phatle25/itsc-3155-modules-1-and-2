
# ask user to put in 2 strings
string1 = input('Enter a string: ')
string2 = input('Enter another string: ')
# find the length of each string
a = len(string1)
b = len(string2)

if a < b and string1[0:a] == string2:
    print("False")
elif a >= b and string2[0:b] == string1:
    print("False")
else:
    print("True")
