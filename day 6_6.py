import random
list_of_numbers=[]
for i in range(10000):
    a=random.randint(1,100)
    if (a not in list_of_numbers):
        list_of_numbers.append(a)
print(list_of_numbers)
print(len(list_of_numbers))



    
    




