import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))

la=['USA','CHINA','INDIA','CANANDA','TURKEY']
values=[25,10,15,40,23]
expld=[0.1,0.2,0.4,0,0]
cols=['c','m','r','#556622','yellow']
plt.pie(values,
        labels=la,
        colors=cols,
        autopct='%.1f%%',
        explode=expld,
        shadow=True,
        startangle=90)


plt.show()
