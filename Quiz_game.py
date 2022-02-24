print('welcome in the quiz game')

ask=input('want to continue ? ').lower()
score=0

if ask!='yes':
    quit()
else:
    print('welcome in my game :) ')

answer=input('what is full form of cpu ? ').lower()
if answer=='central processing unit':
    print('you are write ')
    score+=1
else:
    print('you are wrong!! ')

answer=input('what is full form of gpu ? ').lower()
if answer=='graphics processing unit':
    print('you are write !!')
    score += 1
else:
    print('you are wrong!! ')

answer=input('what is the full form of ram ? ').lower()
if answer=='random axis memory':
    print('you are write !!')
    score += 1
else:
    print('you are wrong !!')

answer=input('what is full form of psu ? ').lower()
if answer=='power supply unit':
    print('you are write!! ')
    score += 1
else:
    print('you are wrong!! ')

print('you got '+str(score)+' question correct')
print( ' your score is '+str((score/4)*100)+'%')
