import random
def userChoice():
    userchoice=input("enter your choice")
    return userchoice

def computerChoice():
    option=('rock','paper','scissors')
    randomNo=random.randint(0,2)
    computerchoice=option[randomNo]
    return computerchoice


def gameplay(userchoice,computerchoice):
    if(userchoice=='rock'and computerchoice=='paper'):
        print("You have WON!!!")
        return 'u'
    elif(userchoice=='paper' and computerchoice=='scissors'):
        print("you have lost")
        return 'c'
    elif(userchoice=='paper' and computerchoice=='rock'):
        print("you have won")
        return 'u'
    elif(userchoice=='scissors' and computerchoice=='paper'):
        print("you have won")
        return 'u'
    elif(userchoice=='rock' and computerchoice=='scissors'):
        print("you have lost")
        return 'c'
    elif(userchoice=='scissors' and computerchoice=='rock'):
        print("you have lost")
        return 'c'
    elif(userchoice=='rock' and computerchoice=='rock'):
        print("SAME RESULT")
    elif(userchoice=='paper' and computerchoice=='paper'):
        print("SAME RESULT")
    elif(userchoice=='scissors' and computerchoice=='scissors'):
        print("SAME RESULT")     
    else:
        print("the entry is invalid")

def scoreBoard(us,cs):
    if(us==1 and cs==0):
        us=us+1
        return us
    else:
        cs=cs+1
        return cs
    
i=1
us=0
cs=0
while(i<=5):
    print("\nWelcome to Rock Paper and Scissor Game:\nPress 'p' to Play and 'q' to exit:")
    step=input()
    if (step == 'q' or step == 'Q'):
        print("Bye!!!")
        break
    elif(step == 'p' or step == 'P'):
        print ("Welcome to Game\nRound : "+str(i))
        uc=userChoice()
        cc=computerChoice()
        print(cc)
        score=gameplay(uc,cc)
        if(score=='u'):
            us=scoreBoard(1,0)
        else:
            cs=scoreBoard(0,1)
        i+=1
    else:
        print("Invalid Choice")
        
    
if(us>cs):
    print("User Wins!!!!")

else:
    print("Computer Wins!!!")

