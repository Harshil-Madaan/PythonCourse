'''listofnames=('Tom','Jerry','John')
def details(names):
    print (names)
details(listofnames)'''
#arbitary arguments
def details(*names):
    for name in names:
        print("hello"+name)
details('Tom','Jerry','John')
