#palindrome
n=int(input("Enter a number:"))
# value of integer is stored in temp variable
temp=n
rev=0
#last digit of no. is obtained by using mod operator
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number is not a plaindrome!")
