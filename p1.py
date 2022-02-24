d={
  'China':143,
 'India':136,
 'USA':32,
 'Pakistan':21}

def func(s):
  if s=='print':
    for k,v in d.items():
      print(k , v)
  elif s=='add':
    a=str(input('enter a country name :'))
    if a not in d.items():
      b=int(input('enter the population :'))
      d[a]=b
      print(d)
    else :
      print('already exist')
  elif s=='remove':
    c=str(input('enter a country name :'))
    if c in d.keys():
      del d[c]
      print(d)
    else:
      print('do not exist in tle dictanary')
  elif s=='query':
    f=str(input('enter a country name :'))
    if f  in d.keys():
      print(d[f])
    else:
      print('do not exist in tle dictanary')  
  else:
    print('you dont put anything')

s=str(input('enter any one between  print ,add, remove, query  :'))    
      
func(s)