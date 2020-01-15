import random
number=random.randint(0,20)
response=int(input("Guess the Number:"))
while(True):
    if(number<response):
        print("Too high")
        break
    elif(number>response):
        print("Too low")
        break
    elif(number==response):
        print("You guessed it right!")
    else:
        print("TRY AGAIN!")
        break
print(number)

    
    
