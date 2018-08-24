import random
num = random.randint(1, 10)
while True:
    print('Guess a number between 1 and 10')
    guess = input()
    i = int(input(guess))
    if i == num:
        print('You won!!!')
        break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')

print('if you gussed less than 6 times you won')