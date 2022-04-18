import random

string="abcdefghijklmnopqrstuvwxyz"
alphabet=""

cipherText = str(input("Enter cipher text: "))
key = input("Enter key: ")

if key == "random":
    a = random.randint(1, 26)
    b = random.randint(1, 26)

else:
    key = key.split(',')
    a = key[0]
    b = key[1]

for i in range(26):
    alphabet+=chr(((a*i+b)%26)+ord('A'))

print(alphabet.lower())

translation = cipherText.maketrans(str(string), str(alphabet))
print((cipherText.translate(translation)).lower())
