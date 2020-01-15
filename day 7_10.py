str1=input("Enter a word:")
strlength=len(str1)
str2=str1[strlength::-1]
if(str1==str2):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
