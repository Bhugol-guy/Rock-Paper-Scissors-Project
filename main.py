import random
c=0
h=0
print('Rock, Scissor and Ppper game with computer.')
lst=['rock','paper','scissor']
while True:
  choice=input('\nEnter Rock/Scissor/Paper or q to quit: ')
  if choice.lower()=="q":
    print('Thank You for Playing !!')
    break
  comp=random.randint(0,2)
  print('\nYour Choice=',choice)
  print('Computer Choice=',lst[comp],'\n')
  if lst[comp]=='rock' and choice.lower()=='scissor':
    print('Computer Wins')
    c+=1
  elif lst[comp]=='paper' and choice.lower()=='rock':
    print('Computer Wins')
    c+=1
  elif lst[comp]=='scissor' and choice.lower()=='paper':
    print('Computer Wins')
    c+=1
  elif lst[comp]=='rock' and choice.lower()=='paper':
    print('You Win ')
    h+=1
  elif lst[comp]=='paper' and choice.lower()=='Scissor':
    print('You Win ')
    h+=1
  elif lst[comp]=='scissor' and choice.lower()=='rock':
    print('You Win ')
    h+=1
  else:
    print('Nobody Won')
print('Your score =',h,'and computer score =',c)
