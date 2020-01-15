#wap to check whether a no. is prime or not
num=int(input("enter a number:"))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
    else:
        print("prime number")
        break
