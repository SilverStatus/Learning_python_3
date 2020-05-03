import random
import string

# create function to random pass
def randompass(stringlenght, strenght):
  if strenght == 'low':
    password = string.ascii_letters + string.digits
    return ''.join(random.choice(password)for i in range(stringlenght))
  elif strenght == 'high':
    password = string.digits + string.punctuation + string.ascii_letters
    return ''.join(random.choice(password)for i in range(stringlenght))

# identify how man characters used for password
b = int(input('password lenght: '))
# identify usage of password
u = input('password usage: ')
# choose strenght of password
s = input('choose password strenght (low or high): ')
# input password in txt file
file_pass = randompass(b,s)
pass_file = open('passfile1.txt', 'a')
pass_file.write(u+' password: '+file_pass+'\n')
pass_file.close()
