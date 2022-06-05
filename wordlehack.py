import re

q = set()


def printer(x, y):
    global q
    print(x, end=" - ")
    s = ""
    for i in x:
        if i not in y:
            s = s + i
            q.add(i)
    print(s)


f1 = open(".\wordledict.txt", "r")

for i in f1.readlines():
    x = list(i.split(","))
    for j in x:
        if 'p' in j and j[1] == 'r' and j[2] == 'e' and j[0]=='c':
            printer(j, [])
print(q)

f1.close()
