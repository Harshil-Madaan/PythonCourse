import random
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
symbols='!@#$%^&*()'
option=('uc','lc','digit','symbol')


numbers=input("Enter the number of integers you want in the password")
letters=input("Enter the number of letters you want in the password")
symbols=input("Enter the number of symbols you want in the password")
password=''
for i in range(int(numbers)):
    value=option[random.randint(0,3)]
    if(value is 'uc'):
        password=password+uppercase[random.randint(0,25)]        
    elif(value is 'lc'):
        password=password+lowercase[random.randint(0,25)]
    elif(value is 'digit'):
        password=password+digits[random.randint(0,8)]
    elif(value is 'symbol'):
        password=password+symbols[random.randint(0,8)]
    else:
        print ('Error')
print("Your Password is: ", password)









