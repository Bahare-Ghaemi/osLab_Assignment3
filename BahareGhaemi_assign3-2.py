from random import random


import random

n = input('enter size of array : ')

numbers = []
e = 1

while n != e:
    number = random.randint(1,100)
    if number in numbers:
        break
    else:
        numbers += [number]
        e = e + 1

print(numbers)