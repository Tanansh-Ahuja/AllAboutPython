import random
import math


#main
f=open('sample.txt','w')
s=''
sign=['+','-']
for i in range(1,601):
    if i<200:
        for j in range(0,11):
            if j%2==0:
                s=s+str(random.randint(1,99))
            else:
                s=s+random.choice(sign)
        if eval(s)>=0:
            f.write(s+'='+str(eval(s)))
            f.write('\n')
        s=''
    elif i<400:
        for j in range(0,21):
            if j%2==0:
                s=s+str(random.randint(1,99))
            else:
                s=s+random.choice(sign)
        if eval(s)>=0:
            f.write(s+'='+str(eval(s)))
            f.write('\n')
        s=''
    else:
        for j in range(0,31):
            if j%2==0:
                s=s+str(random.randint(1,99))
            else:
                s=s+random.choice(sign)
        if eval(s)>=0:
            f.write(s+'='+str(eval(s)))
            f.write('\n')
        s=''

f.close()
