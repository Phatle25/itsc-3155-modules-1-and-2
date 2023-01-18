 #enter string
string=input("Enter a string: ")
 #split the string into list
stringList=list(string)
#empty list
fullnewstringlist=[] 
for k in range(0,len(stringList),3): #loop from 0 to length of stringList
    #empty list
    newstringlist=[] 
     #loop from 0 to 3
    for i in range(0,3):
        #if k+i is less than length of stringList
        if (k+i)<len(stringList): 
            #append value of stringList : k+i index to newstringlist
            newstringlist.append(stringList[k+i])
    #append newstringlist to fullnewstringlist         
    fullnewstringlist.append(newstringlist) 
#display fullnewstringlist    
print(fullnewstringlist) 