import random
import string

x=input("Enter the text you want to encode: ")
d=""
e = int(random.randint(1,25))
c=str(input("Enter the key: "))
string = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = [0 for y in range(26)]

def snip_string(d, n):
    list_string = list(d)
    list_string.sort()
    chars = set(d)
    for char in chars:
        while list_string.count(char) > n:
            list_string.remove(char)
    return ''.join(list_string)

def split(word):
    return [char for char in word]

d=""

if c == "random" and (x.islower()):
    for i in range(1, e):
        e = int(random.randint(1,25))
        d += string[e]



    text=snip_string(d, 1)


    text = split(text)

    for i in range(len(text)):
        count[ord(text[i])-97] += 1

    mis=""
    for i in range(0,26):
        if count[i] == 0:
            mis+=string[i]

    mis=split(mis)
    alphabet=str(text + mis)

    " ".join(alphabet.split())

    translation = x.maketrans(str(string), str(alphabet))
    print(x.translate(translation))

elif c == "random" and (x.isupper()):
    print("Please enter a number in the lower case")

elif c != "random" and x.isalpha():

    c=snip_string(c, 1)
    c=split(c)
    for i in range(len(c)):
        count[ord(c[i])-97] += 1

    mis=""
    for i in range(0,26):
        if count[i] == 0:
            mis+=string[i]

    mis=split(mis)
    alphabet=str(c + mis)

    " ".join(alphabet.split())

    translation = x.maketrans(str(string), str(alphabet))
    print(x.translate(translation))
