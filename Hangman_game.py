# hangman game program
import time
import random
name = input('name: ')
print('Hello '+ name + ' Welcome to game ')
time.sleep(1)
print('start guessing')
time.sleep(0.5)
print('===============')
# set secret word
list_word = ['cat', 'dog', 'fish']
word = random.choice(list_word)

# defining clues as function 
def guide():
  print('Here are the clue')
  if word == 'cat':
    print('it is pet')
    print('it has claw')
    print('it likes to sleep and eat')
  elif word == 'dog':
    print('it is pet')
    print('people said it is man best friends')
    print('it is smart pet')
  else:
    print('it is pet')
    print('it lives in water')
    print('it has beautiful color')

# empty variable
guesses = ''
# defining turn
turns = 5
# calling clues function
guide()
print('================')
#check if the turns are more than zero
while turns > 0:
  # count start with 0
  failed = 0
  for char in word:
    if char in guesses:
      print(char, end = '')
    else:
      print('-', end = '')
      failed += 1
  if failed == 0:
    print('')
    print('you won')
    break
  print('')
  # input from user
  guess = input('guess character:')
  guesses += guess
  if guess not in word:
    turns -= 1
    print('wrong')
    print('you have', +turns, 'more guesses')
    if turns == 0:
      print('you lose')
