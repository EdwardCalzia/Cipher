import numpy as np
import matplotlib.pyplot as plt
def split(word):
    return [char for char in word]
x=input("")
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = split(x)
print(x)
for i in range(len(x)):
    count[ord(x[i])-97] += 1

print(count)
y=len(x)
print(y)


top=[('a',1.875),('c',1.125),('d',0.5),('e',0.5),('f',0.5),('g',0.5),('h',0.5),('i',0.5),('j',0.5),('k',0.5),('l',0.5),('m',0.5),('n',0.5),('o',0.5),('p',0.5),('q',0.5),('r',0.5),('s',0.5),('t',0.5),('u',0.5),('v',0.5),('w',0.5),('x',0.5),('y',0.5),('z',0.5)]

labels, ys = zip(*top)
xs = np.arange(len(labels)) 
width = 1

fig = plt.figure()                                                               
ax = fig.gca()
ax.bar(xs, ys, width, align='center')
ax.set_xticks(xs)
ax.set_xticklabels(labels)
ax.set_yticks(ys)

plt.show()
