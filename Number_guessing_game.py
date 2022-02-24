import random

num=input('enter a numner :')

if num.isdigit():
    num=int(num)
    if num<0:
        print('please enter a positive number next time !')
        quit()
else:
    print('enter a number next time ')
    quit()

random_number=random.randint(0,num)
guesses=0
while True:
    guesses +=1
    guess=input('guess a random number :')
    if guess.isdigit():
        guess=int(guess)
    else:
        print('enter a number next time ')

    if guess==random_number:
        print('wow!! you got it correct')
        break
    elif guess<num:
        print('you are bellow the no ')
    else:
        print('you are above the no ')


print('you got it in ',guesses,'attempt')