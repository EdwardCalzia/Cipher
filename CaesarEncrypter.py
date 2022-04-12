import random

b=input("Enter the text you want to encode: ")

c=int(input("Enter the key: "))
d=""
e = int(random.randint(1,26))
  
if c == 0 and (b.islower()):
    for i in range(len(b)):
        d += chr((ord(b[i]) + int(e)) % 26 + 97)
    print("The encoded text is: " + d)

elif c == 0 and (b.isupper()):
    print("Please enter a number in the lower case")

if any(i == c for i in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)) and (b.islower()):
    c=c+7
    for i in range(len(b)):
        d += chr((ord(b[i]) + int(c)) % 26 + 97)
    print("The encoded text is: " + d)

if any(i == c for i in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)) and (b.isupper()):
    print("Please enter a number in the lower case")
