import matplotlib.pyplot as plt
import numpy as np
#Part 1
'''
import csv


x=[]
y=[]
with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
'''

#Part 2
x,y=np.loadtxt('example.txt', delimiter = ',' ,unpack=True)
plt.plot(x,y)



plt.xlabel('plot x')
plt.ylabel('plot y')
plt.title('Intresting Graph\nCheck it out')
#plt.legend()
plt.show()
