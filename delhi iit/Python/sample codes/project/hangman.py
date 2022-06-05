import random
import string

r_words=['triangle','grandeur','hogwarts','damsel','animesh','billbook']
word=''
w_c=''
w_w=['a','e','i','o','u']
score=3
def gen_puzzle():
    global w_c
    w_c=word
    for w in w_c:
        if w not in w_w:
            w_c=w_c.replace(w,' _ ')
    print w_c

def input_word():
    global w_c
    global score
    word_g = raw_input("Enter Word: ")
    if word_g in word:
        w_w.append(word_g)
        print"Correct!!"
    else:
        print"Wrong!"
        score-=1

def puzzle():
    global score
    global word
    word=r_words[random.randint(0,len(r_words)-1)]
    while score>0:
        gen_puzzle()
        if w_c==word:
            print"You Won!!"
            break
        else:
            input_word()
        if score==0:
            print"You Loose!!"

puzzle()
