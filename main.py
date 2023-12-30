#Password Generator Project
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised
ltr = ''
sym = ''
num = ''
for i in range(0,nr_letters):
  a = random.choice(letters)
  ltr += a

for i in range(0,nr_symbols):
  a = random.choice(symbols)
  sym += a

for i in range(0,nr_numbers):
  a = random.choice(numbers)
  num += a

ezy_password = ltr+sym+num

print(f"\n=>Easy Password is: {ezy_password}")

#Hard password : Order randomised

hard_password_1 = ""
hard_password = ""
sfl = []
for i in ezy_password:
  sfl.append(i)


rad = random.shuffle(sfl)

for i in range(0, len(sfl)):
  hard_password_1 += sfl[i]

print(f"\n=>Hard Password Choice 1 is: {hard_password_1}")

sfl_num= []

for i in range(0,len(sfl)):
  rnd = random.randint(0, len(sfl)-1)
  while rnd in sfl_num:
    rnd = random.randint(0, len(sfl)-1)
  sfl_num.append(rnd)


"""for i in range(0,len(sfl)):
  rnd = random.randint(0, len(sfl)-1)
  if rnd in sfl_num:
    while rnd in sfl_num:
      rnd = random.randint(0, len(sfl)-1)
    sfl_num.append(rnd)
  else:
    sfl_num.append(rnd)"""


for i in sfl_num:
  hard_password += sfl[i]

print(f"\n=>Hard Password Choice 2 is: {hard_password}")

sys.exit()