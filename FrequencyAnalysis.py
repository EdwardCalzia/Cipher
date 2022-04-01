import numpy as np
import matplotlib.pyplot as plt

def split(word):
    return [char for char in word]
x=input("")

count = [0 for y in range(26)]

x = split(x)

print(x)

for i in range(len(x)):
    count[ord(x[i])-97] += 1

print(count)
y=len(x)
print(y)


top=[('a',count[0]),('b',count[1]),('c',count[2]),('d',count[3]),('e',count[4]),('f',count[5]),('g',count[6]),('h',count[7]),('i',count[8]),('j',count[9]),('k',count[10]),('l',count[11]),('m',count[12]),('n',count[13]),('o',count[14]),('p',count[15]),('q',count[16]),('r',count[17]),('s',count[18]),('t',count[19]),('u',count[20]),('v',count[21]),('w',count[22]),('x',count[23]),('y',count[24]),('z',count[25])]

labels, ys = zip(*top)
xs = np.arange(len(labels)) 
width = 0.8

fig = plt.figure()                                                               
ax = fig.gca()
ax.bar(xs, ys, width, align='center')
ax.set_xticks(xs)
ax.set_xticklabels(labels)
ax.set_yticks(ys)

plt.show()
