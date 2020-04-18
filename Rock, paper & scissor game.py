import random
options = ['paper', 'rock', 'scissor']
computer_choice = random.choice(options)
# check reslut from randowm module
# print(computer_choice)
print('game will run 3 times')
# game will run max 3 times
total_score = 0
score = 0
for i in range(3):
  print('choose one :' +str(options))
  print('input options: ')
  choice = input()
  # check Value
  if choice == 'paper':
    if computer_choice == 'rock':
      print('congratulation! you win!')
      score += 2
    elif computer_choice == 'scissor':
      print('sorry you lose')
      #score += 0
    else:
      print('draw')
      score += 1
  #paper_total_score += score
  elif choice == 'rock':
    if computer_choice == 'paper':
      print('sorry you lose')
      #score += 0
    elif computer_choice == 'scissor':
      print('congratulation! you win!')
      score += 2
    else:
      print('draw')
      score += 1
  #rock_total_score += score    
  elif choice == 'scissor':
    if computer_choice == 'rock':
      print('sorry you lose')
      #score += 0
    elif computer_choice == 'paper':
      print('congratulation! you win!')
      score += 2
    else:
      print('draw')
      score += 1
  #scissor_total_score += score
  elif choice == 'quit':
    print('exit game')
    break
  else:
    break
# calculate total score
total_score += score
  
print('=====================================')  
print('your final score: '+ str(total_score))


  

