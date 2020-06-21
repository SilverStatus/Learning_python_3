import random

print("welcome to dice game")
a = input("how many times to roll dice: ")
i = 0
for i in range(int(a)):
  buah = random.randint(1, 6)
  i += 1
print('result of '+ str(i) +' times rolling dice: ' + str(buah))
