# ask user to type in their grade from 0 to 100
grade = input("Enter your grade from 0 to 100: ")
# set the grade to be any number
score = float(grade)
# use if else statement to set up the grade letter condition
try:
    if score >= 90 and score <= 100: 
        print("Your grade is A")
    elif score >= 80 and score <= 89:
        print("Your grade is B")
    elif score >= 70 and score <= 79:
        print("Your grade is C")
    elif score >= 60 and score <= 99:
        print("Your grade is D")
    else:
        print("Your grade is F! Sorry! You failed!")
except:
    print("Error") 
    # error if users add any number less than 0 and bigger than 100. 
