import random
number=random.randint(1,10)
print (number)
response=int(input("Guess the Number"))
while (True):
    if(number == response):
        print ("Yahh!!! You Guess is correct")
        break
    else:
        print("Try Again!!!")
        response=int(input("Guess the Number"))

