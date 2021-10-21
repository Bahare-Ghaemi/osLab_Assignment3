user_num = int(input('enter a number : '))

sum1 = 1
sum_ = 1
e = 0

while True:
    sum_ *= sum1
    if sum_ == user_num :
        print('yes')
        break
    if sum_ > user_num:
        print('no')
        break
    sum1 = sum1 + 1
