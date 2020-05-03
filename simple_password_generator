import random
import string

# create function to random pass
def randompass(stringlenght):
  # creat password with combinarion of alphabet, number and special characters
  password = string.digits + string.punctuation + string.ascii_letters
  return ''.join(random.choice(password)for i in range(stringlenght))

# identify how man characters used for password
b = int(input('password lenght: '))
file_pass = randompass(b)
pass_file = open('passfile.txt', 'w')
pass_file.write('password: '+file_pass)
pass_file.close()
