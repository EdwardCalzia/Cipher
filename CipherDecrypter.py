words = {
    'all': 2828, 'think': 180, 'just': 123, 'when': 577, 'over': 646, 'also': 85, 'only': 372, 'has': 419,
    'them': 530, 'his': 3907, 'get': 242, 'know': 331, 'they': 572, 'not': 1466, 'now': 1030, 'him': 1267,
    'like': 685, 'this': 1273, 'good': 200, 'she': 523, 'because': 73, 'people': 42, 'back': 208,
    'see': 1004, 'are': 1001, 'year': 116, 'out': 1429, 'even': 303, 'what': 510, 'for': 2448, 'then': 592, 'new': 123, 'who': 616, 'use': 372, 'come': 255, 'about': 310, 'would': 427, 'could': 221,
    'first': 207, 'into': 529, 'one': 1640, 'your': 275, 'from': 1039, 'her': 3411, 'there': 802, 'two': 289, 'been': 408, 'their': 610, 'way': 660, 'was': 1655, 'that': 2943, 'some': 888,
    'with': 1907, 'than': 424, 'must': 289, 'made': 177, 'look': 322, 'these': 373, 'work': 122, 'say': 329, 'will': 389, 'can': 528, 'were': 716,
    'and': 7377, 'give': 126, 'have': 757, 'any': 591, 'want': 65, 'make': 157, 'how': 422, 'other': 632, 'take': 222,
    'which': 623, 'you': 1204, 'our': 941, 'after': 296, 'most': 532, 'the': 18475, 'well': 217, 'time': 570
}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x=input("Enter the text you want to decode: ")
amount=0
count=""
for i in range(1,26):
    d=""
    for e in range(len(x)):
        d += chr((ord(x[e]) + int(i)) % 26 + 97)

    if any(word in d for word in words):
        count += "\n" + d + "\n"
        amount+=1
    
    if amount == 0:
        pass
    else:
        print(count)
    
    amount = 0
