n=input("enter the length in cm")
n=int(n)
if(n>=0):
    a=n%2.54
    print(a)
    print("the length in inches is:",a)
else:
    print("the entry is invalid")
