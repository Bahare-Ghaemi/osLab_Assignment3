numbers = []

while True :
    number = input ('enter a number (enter n to exit) : ')
    if number == 'n':
        break
    numbers += [number]

number_0 = numbers[0]
e = 1

for number in numbers:
    if number_0 > number:
        e = 0
        break
    number_0 = number

if e == 1:
    print ('your array is regular')
else:
    print ('your array is NOT regular')