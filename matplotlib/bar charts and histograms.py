import matplotlib.pyplot as plt



x=[2,4,6,8,10]
y=[6,7,30,20,5]

x2=[1,3,5,7,9]
y2=[5,6,3,12,16]

plt.bar(x,y,label='bars 1',color='blue')
plt.bar(x2,y2, label='bars 2',color='red')
#i can color my graph as i want. hex colors are also there
plt.xlabel('Plot x')

plt.ylabel('Plot y')

plt.title('Intresting graph\nCheck it out')
plt.legend()
#plt.legend() is used so that it shows that first line and second line thing

plt.show()

