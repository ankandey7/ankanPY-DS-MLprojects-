pwd=input('enter your master paswoed :')

def view():
    pass

def add():
    pass

while True:
    mode=str(input('would you like to add a new password or view exixting ones (add/view) or type q to quit :')).lower()
    if mode=='q':
        break

    if mode=='add':
        pass
    elif mode==view:
        pass
    else:
        print('invalid input ')
        continue


