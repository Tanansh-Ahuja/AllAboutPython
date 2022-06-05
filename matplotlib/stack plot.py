import matplotlib.pyplot as plt


days=[1,2,3,4,5]
sleeping=[7,8,6,11,9]
eating=[2,5,3,5,4]
working=[7,8,7,2,2]
playing=[1,2,1,3,0]

plt.stackplot(days, sleeping, eating, working, playing, colors=['magenta','red','yellow','green'])



plt.xlabel('Plot x')

plt.ylabel('Plot y')

plt.title('Intresting graph\nCheck it out')
#plt.legend()
#plt.legend() is used so that it shows that first line and second line thing

plt.show()

