import  random

user_unis=0
computer_unis=0
options=['rock','paper','scissor']

while True:
    user_input=input('Type rock/paper/scissor or type q to quit :').lower()
    if user_input=='q':
        break

    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    #rock:0,paper:1,scissors:2
    computer_pick=options[random_number]
    print('computer picked ',computer_pick)

    if user_input=='rock' and computer_pick=='paper':
        print('you won !')
        user_unis +=1


    elif user_input=='paper' and computer_pick=='rock':
        print('you won !')
        user_unis +=1


    elif user_input=='scissors' and computer_pick=='paper':
        print('you won !')
        user_unis +=1

    else:
        print('computer wins !')
        computer_unis+=1

print(' you won ',user_unis ,'times')
print('computer won',computer_unis,'times')
print('good bye !')
