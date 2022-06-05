import matplotlib.pyplot as plt



x=[1,2,3]
y=[4,2,7]

x2=[1,2,3]
y2=[11,15,18]

plt.plot(x,y, label='First line')
plt.plot(x2,y2, label='Second line')

plt.xlabel('Plot x')

plt.ylabel('Plot y')

plt.title('Intresting graph\nCheck it out')
plt.legend()
#plt.legend() is used so that it shows that first line and second line thing

plt.show()

