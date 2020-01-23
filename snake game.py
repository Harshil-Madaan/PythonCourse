import time
import random
import pygame

#importing pygame
pygame.init() #initializing pygame

#making the canvas
canvasHeight=600
canvasWidth=600
canvas=pygame.display.set_mode((canvasHeight,canvasWidth))
pygame.display.update()
pygame.display.set_caption("My snake game")
#Colors 
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)  



#snake size
snakesize=10
snakeSpeed=10



clock=pygame.time.Clock()

#Font Styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#all user defined function
def message(msg,color):
    msg=font_style.render(msg,True,color)
    canvas.blit(msg,[10,300])
def CurrentSnake(snakesize,snakeList):
    for x in snakeList:
        pygame.draw.rect(canvas,black,[x[0],x[1],snakesize,snakesize])#1-canvas,2-color,3.1-x axis,3.2-y axis,3.3-width,3.4-height

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    canvas.blit(value, [0, 0])
    
#main game loop
def gameLoop():
    gameOver=False
    gameClose=False
    
    #snake initial position
    posX=int(canvasHeight/2)
    posY=int(canvasWidth/2)
    
    changeX=0
    changeY=0
    
    #snake length
    snakeList=[]
    snakeLength=1

    #food pos
    foodX=round(random.randrange(0, canvasWidth - snakesize) / 10.0)*10 
    foodY=round(random.randrange(0, canvasHeight - snakesize) / 10.0) *10

    
#main method

    while not gameOver:
        while gameClose==True:
            canvas.fill(blue)
            message("You lost!!! Press Q to quit or P to play again",red)
            Your_score(snakeLength-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    gameOver=True
                    gameClose=False
                if event.key==pygame.K_p:
                    gameLoop()
            
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    changeX=-snakesize
                    changeY=0
                elif event.key==pygame.K_RIGHT:
                    changeX=snakesize
                    changeY=0
                elif event.key==pygame.K_UP:
                    changeX=0
                    changeY=-snakesize
                elif event.key==pygame.K_DOWN:
                    changeX=0
                    changeY=snakesize
                    
        if (posX >= canvasWidth) or (posX < 0) or (posY >= canvasHeight) or (posY<0):
            gameClose=True
            #score=snakeLength-1
            #return score

        posX+=changeX
        posY+=changeY
        canvas.fill(blue)
        pygame.draw.rect(canvas,red,[foodX,foodY,snakesize,snakesize])
        snakeHead=[]
        snakeHead.append(posX)
        snakeHead.append(posY)
        snakeList.append(snakeHead)
        if len(snakeList)> snakeLength:
            del snakeList[0]
        for x in snakeList[ :-1]:
            if x==snakeHead:
                gameClose=True
        CurrentSnake(snakesize,snakeList)
        Your_score(snakeLength- 1)
        pygame.display.update()
        
        if(posX==foodX) and (posY==foodY):
            foodX=round(random.randrange(0, canvasWidth - snakesize) / 10.0)*10 
            foodY=round(random.randrange(0, canvasHeight - snakesize) / 10.0) *10
            snakeLength+=1
        clock.tick(snakeSpeed)   

    pygame.quit()
    quit()
gameLoop()
#print (x)
