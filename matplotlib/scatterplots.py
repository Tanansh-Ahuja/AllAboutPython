import matplotlib.pyplot as plt



x=[1,2,3,4,5,6,7,8]
y=[3,7,5,12,15,43,78,50]
plt.scatter(x,y,label='yup',color='cyan',marker='+',s=100)
#marker keyword helps us choose a marker of our own choice.
#   's' is used to change marker size
# you can look up to google to see how many types of markers are there

plt.xlabel('Plot x')

plt.ylabel('Plot y')

plt.title('Intresting graph\nCheck it out')
plt.legend()
#plt.legend() is used so that it shows that first line and second line thing

plt.show()

