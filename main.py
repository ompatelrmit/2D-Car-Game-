import random
import pygame
from pygame import  mixer
from sys import exit
import time 
pygame.init()
#screen height and width
hidth = 300
width = 500
screen = pygame.display.set_mode((hidth, width))

#display background and caption 
pygame.display.set_caption('Car Game')
background = pygame.image.load('background.png')


#taxi spwn
taxi = []
taxiX = []
taxiY = []
taxiY_ch = []
taxiX_ch = []
taxirect = []
taxi_spwn = 2
b = 0
i=0
for i in range(taxi_spwn):
    taxi.append(pygame.image.load('car.png'))
    taxiX.append(0)
    taxiY.append(random.choice([20, 110, 210]))
    taxiX_ch.append(-0.4)
    taxiY_ch.append(-1)
    taxirect.append(pygame.Rect(0, 0, 0, 0))
    b = 1

#truck spwn
i=0 
truck = pygame.image.load('truck.png')
truck=pygame.transform.scale(truck,(75,70))
truck_height = 64
truck_width = 64
truckY = 0
truckX = 0
truckY_ch = random.choice([20, 110, 210])
for i in range(taxi_spwn):
    while truckY_ch==taxiY[i]:
         truckY_ch=random.choice([20, 110, 210])
         print(truckY_ch,taxiY)
truckY=truckY_ch
truckX_ch = -0.4
truckrect = pygame.Rect(0, 0, 0, 0)

#this is moveable main car 
sps = pygame.image.load('car2.png')
sps_height = 80
sps_width = 80
sps = pygame.transform.scale(sps, (sps_width, sps_height))
spsY = 110
spsX = 430
spsY_ch = 0
spsX_ch = 0
a = 0
score=0
score_text=pygame.font.Font('freesansbold.ttf', 20)


#this is some text that we want to display in screen 
clock = pygame.time.Clock()
over_font = pygame.font.Font('freesansbold.ttf', 45)
instruction = pygame.font.Font('freesansbold.ttf', 14)
instruction_text = instruction.render("PRESS SPACE KEY TO START GAME", True, (255, 255, 255))
fps = 60
c = 1

#car blit funcion
def s(spsy, spsx):
    screen.blit(sps, (spsy, spsx))

#taxi blit funcion
def t(taxiy, taxix, k):
    global taxirect
    screen.blit(taxi[k], (taxiy, taxix))
    taxirect[k] = pygame.Rect(taxiY[k] + 15, taxiX[k], 31, 56)

#game over text and some instrction that we want to display
def game_over():
    global event, run
    screen.blit(background, (0, 0))
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (10, 250))
    screen.blit(instruction_text, (17, 300))
    text1=score_text.render(str("Total score :"),True,(255,255,255),None)
    screen.blit(text1,(70,200))
    text=score_text.render(str(score),True,(255,0,0),None)
    screen.blit(text,(200,200))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    waiting = False

#when we first we start our game this function is display
def star():
    global run, event
    screen.blit(instruction_text, (17, 200))
    pygame.display.flip()
    screen.blit(background, (0, 0))
    wait = True
    while wait:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                 if event.key==pygame.K_SPACE:
                    wait = False


#truck blit funcion
def ta(trucky, truckx):
    global truckrect
    screen.blit(truck, (trucky, truckx))
    truckrect = pygame.Rect(truckY + 7, truckX, 60, 60)


start2 = True
run = True

#this is our main loop
while run:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    #this is used for when game is over and first time game is start then this function is called
    if start2:

        #this is used when we first time start game the start function called only once time
        if c == 1:
            star()
            c = 0
            pass
        start2 = False
        
        #this is used for when game is over it respwning the all objcet
        truckY = random.choice([20, 110, 210])
        truckX = 0
        truckY_ch = -1
        truckX_ch = -0.4
        truckrect = pygame.Rect(0, 0, 0, 0)
        taxi = []
        taxiX = []
        taxiY = []
        taxiY_ch = []
        taxiX_ch = []
        taxirect = []
        taxi_spwn = 2
        b = 0
        for i in range(taxi_spwn):
            taxi.append(pygame.image.load('car.png'))
            taxiX.append(random.choice([20, 110, 210]))
            taxiY.append(0)
            while taxiY[i] == truckY:
                taxiY[i] = random.choice([20, 110, 210])
                if b == 1:
                    while taxiY[i - 1] == truckY:
                        truckY = random.choice([20, 110, 210])
            taxiX_ch.append(-0.4)
            taxiY_ch.append(-1)
            taxirect.append(pygame.Rect(0, 0, 0, 0))
        sps = pygame.image.load('car2.png')
        sps_height = 80
        sps_width = 80
        sps = pygame.transform.scale(sps, (sps_width, sps_height))
        spsY = 110
        spsX = 430
        spsY_ch = 0
        spsX_ch = 0
        score=0
        

    #this is our event in this event we use many button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #this is used for when key is press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                spsY_ch += 0.6
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                spsY_ch -= 0.6
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                spsX_ch -= 0.6
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                spsX_ch += 0.6

        #this is used for when key is realse
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key==pygame.K_w or event.key==pygame.K_s or event.key==pygame.K_a or event.key==pygame.K_d:
                spsX_ch = 0
                spsY_ch = 0

    #this for car boundary so that car does't go out from the screen
    spsY += spsY_ch
    if spsY <= 0:
        spsY = 0
    if spsY >= 220:
        spsY = 220
    spsX += spsX_ch
    if spsX <= 260:
        spsX = 260
    elif spsX >= 420:
        spsX = 420
    s(spsY, spsX)
    spsrect = pygame.Rect(spsY + 16, spsX + 5, 45, 70)

    #this for truck bounary and truck respwn 
    truckX -= truckX_ch
    if truckY <= 0:
        truckY = 0
    if truckY >= 236:
        truckY = 236
    if truckX <= 0:
        truckX = 0
    if truckX >= 439:
        truckX = 0
        truckY_ch = random.choice([20, 110, 210])
        #this is check whether the truck is collision with the taxi or not 
        for i in range(taxi_spwn):
            while truckY_ch==taxiY_ch[i]:
                if truckY_ch==taxiY_ch[i]:
                    truckY_ch=random.choice([20, 110, 210])
                    # print(truckY_ch,taxiY) Used For the Debugging Purpose

        truckX_ch=truckX_ch-0.01
        truckY = truckY_ch
        score+=2
    ta(truckY, truckX)

    #this for taxi boundary and respwn
    for i in range(taxi_spwn):
        taxiX[i] -= taxiX_ch[i]
        if taxiY[i] <= 0:
            taxiY[i] = 0
        if taxiY[i] >= 236:
            taxiY[i] = 236
        if taxiX[i] <= 0:
            taxiX[i] = 0
        if taxiX[i] >= 439:
            taxiX[i] = 0
            taxiY_ch[i] = random.choice([20, 110, 210])
            #this is check whether the taxi is collision with the truck or not 
            while taxiY_ch[i] == truckY_ch:
                taxiY_ch[i] = random.choice([20, 110, 210])
                pass
                if a == 1:
                    while taxiY_ch[i-1]==truckY_ch:
                        taxiY_ch[i-1]= random.choice([20, 110, 210])
                        taxiY[i-1]=taxiY_ch[i-1]
                        t(taxiY[i-1],taxiX[i-1])
            taxiX_ch[i]=taxiX_ch[i]-0.01
            taxiY[i] = taxiY_ch[i]
            score+=2
        t(taxiY[i], taxiX[i], i)
        #this above one commant is used for testing purpose
        #pygame.draw.rect(screen, (255, 0, 255), taxirect[i])

        #this is used for when taxi is colliting with car or not if yes then we call game over function
        if pygame.Rect.colliderect(spsrect, taxirect[i]):
            start2 = True
            crash_sound=mixer.Sound('crash_sound.wav')
            crash_sound.play()
            pygame.time.wait(1000)
            game_over()
    text1=score_text.render(str("score :"),True,(255,255,255),None)
    screen.blit(text1,(180,0))
    text=score_text.render(str(score),True,(255,0,0),None)
    screen.blit(text,(250,0))
            
    #this above two commant is used for testing the purpose
    #pygame.draw.rect(screen, (255, 0, 0), truckrect)
    #pygame.draw.rect(screen, (0, 255, 255), spsrect)

    # #this is used for when truck is colliting with car or not if yes then we call game over function
    if pygame.Rect.colliderect(spsrect, truckrect):
        start2 = True
        crash_sound=mixer.Sound('crash_sound.wav')
        crash_sound.play()
        time.sleep(1)
        game_over()
    
    pygame.display.update()
pygame.quit()
