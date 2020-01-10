maths=input("marks obtained in maths:")
english=input("marks obtained in english:")
physics=input("marks obtained in physics:")
biology=input("marks obtained in biology:")
chemistry=input("marks obtained in chemistry:")
sum=int(maths)+int(english)+int(physics)+int(biology)+int(chemistry)
print(sum)
average=sum/5
print(average)
if(average>=85):
    print("A+")
elif((average>=75) and (average<=84)):
    print("A")
elif((average>=65) and (average<=74)):
    print("B+")
elif((average>=60) and (average<=64)):
    print("B")
elif((average>=50) and (average<=59)):
    print("C")
else:
    print("FAIL")
