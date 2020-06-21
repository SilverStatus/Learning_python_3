# add contacts programs
print('phone book contacts')
contacts = input('how many contacts to add: ')
#create empty dictionary
phone_book = {}
i = 0
for i in range(int(contacts)): 
  a = input('name: ')
  b = input('number: ')
  phone_book[a] = b
print(phone_book)
