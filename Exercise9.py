
#string variable
string = ""
# for loop that loops 5 times from 1 to 5
for i in range(5):
 #reading the word and concatenating with words
    print("Enter a word: ".format(i), end="")
    string = string + " " + input()

print("Words: ", string.split()) #split function to slit string to words
print("One String: ", string) #printing the concatenated word
