from random import randint

while True:
    answer = randint(1, 10)
    try:
        guess = int(input('Guess a number: '))
        if 0 < guess < 11:
            if guess == answer:
                print('You are a genius')
                break
            else:
                print('Wrong')
    except ValueError:
        print('Please enter a number')
        continue
