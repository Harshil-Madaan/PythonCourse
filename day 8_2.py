ofile=open("1.txt","w+")

while(True):
    a=input("Enter Q to Quit:")
    if(a == "q" or a == 'Q'):
        break
    else:
        ofile.write(a)
        print("Saved")
        
ofile.close()

