import matplotlib.pyplot as plt



age=[2,45,34,76,89,78,65,34,56,90,12,120,55,64,32,76,78,43,89,13,44]
#ids=[x for x in range(len(age))]
#plt.bar(ids,age)

bins=[0,10,20,30,40,50,60,70,80,90,100,120,130]

plt.hist(age,bins,histtype='bar',rwidth=0.7)


plt.xlabel('Plot x')

plt.ylabel('Plot y')

plt.title('Intresting graph\nCheck it out')
#plt.legend()
#plt.legend() is used so that it shows that first line and second line thing

plt.show()

