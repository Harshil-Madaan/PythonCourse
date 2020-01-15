def display(number):
    if(number>=0):
        display(number-1)
        print(number)
display(5)
