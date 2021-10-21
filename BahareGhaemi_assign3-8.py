
num1 = int(input('enter bigger number : '))
num2 = int(input('enter smaller number : '))

def KMM_func(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            bmm = i  
    kmm = (x * y) / bmm   
    return kmm 
 
print (KMM_func(num1,num2))