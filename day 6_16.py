def perform(operation):
    num=int(input("Enter the number:"))
    if(operation == 'fact'):
        factorial=1
        if num<0:
            print("Sorry,the factorial of a negative number does not exist")
        elif num==0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,num+1):
                factorial=factorial*i
            print("the factorial of",num,"is",factorial)
    elif(operation == 'armstrong'):
        order=len(str(num))
        sum=0
        temp=num
        while temp>0:
            digit=temp%10
            sum+=digit**order
            temp//=10
        if num==sum:
            print("is an armstrong no.",num)
        else:
            print("is not an armstrong number",num)
    elif(operation == 'prime'):
        for i in range(2,num):
            if num%i==0:
                print("not a prime number")
                break
            else:
                print("prime number")
                break
    elif(operation == 'palindrome'):
        temp=num
        rev=0
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num=num//10
        if(temp==rev):
            print("The number is a palindrome!")
        else:
            print("The number is not a plaindrome!")
        
    

while(True):
    print("\nEnter \"F\" for Factorial of a number \nEnter \"A\"to check whether the number is an armstrong number\nEnter \"P\" to check whether the number is a Prime number \nEnter 'B' to check whether the number is Palindrome")
    choice=input("Enter your choice")
    if(choice=='F' or choice=='f'):
        perform('fact')
    elif(choice=='A'or choice=='a'):
        perform('armstrong')
    elif(choice=='P'or choice=='p'):
        perform('prime')
    elif(choice=='B'or choice=='b'):
        perform("palindrome")
    else:
        print("PLEASE ENTER A VALID CHOICE")
    
        
    

    

    
    
    
    
    
