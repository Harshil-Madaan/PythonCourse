fopen=open("testInput.txt", 'r+')
fopen.write("hello")
for line in fopen:
    print(line,end='')   




'''
print("Enter W for Write and R for read: ")
choice=input()
if(choice=='w' or choice=='W'):
    inputdata=input("Enter Details: ")
    fopen.write(inputdata)
    print ("Saved!!!")    
elif(choice=='r'or choice=='R'):
    for line in fopen:
        print(line,end='')   
else:
    print ("enter the valid Choice")
'''
fopen.close()
