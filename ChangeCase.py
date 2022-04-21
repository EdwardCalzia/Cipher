string = str(input("Enter a text: "))
newstring ='' 

for a in string: 
    if (a.isupper()) == True: 
        newstring+=(a.lower()) 
          
    elif (a.islower()) == True: 
        newstring+=(a.upper())
          
    elif (a.isspace()) == True:
        a.replace(" ", "")

print(newstring)
