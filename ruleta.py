import pygame, random, sys, time, os, subprocess, glob
import RPi.GPIO as GPIO
from pygame.locals import *

screenW=1280
screenH=1000

######### Configuracion de la pantalla
gameDisplay=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('Boliranas El Original')


pygame.init()



greendark=(0,128,0)
bluedark=(0,0,128)
reddark=(128,0,0)
magentadark=(128,0,128)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
magenta=(255,0,255)

blue2=(0,90,255)
orange2 = (255,195,0)
magenta2=(255,0,90)
mangobiche=(255,255,51)
blue3=(26,0,179)


yellow=(255,255,0)

black=(0,0,0)
white=(255,255,255)

#gameDisplay.blit(pygame.image.load('ruleta.png'),(415,250))
posx = list(range(8))
posy = list(range(8))
posx[0]=715
posy[0]=230
posx[1]=810
posy[1]=330
posx[2]=810
posy[2]=465
posx[3]=715
posy[3]=568
posx[4]=568
posy[4]=568
posx[5]=470
posy[5]=465
posx[6]=470
posy[6]=330
posx[7]=568
posy[7]=228

posibles = [300,350,400,450,300,350,400,450]
vivo = [green,blue,red,magenta,green,blue,red,magenta]
muerto = [greendark,bluedark,reddark,magentadark,greendark,bluedark,reddark,magentadark]

ruletaFont = pygame.font.Font(None,165)
posiblesFont= pygame.font.Font(None,80)

radio=65
ajustx=48
ajusty=30
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                
    pygame.draw.circle(gameDisplay, orange2, [640,400],250)
    pygame.draw.circle(gameDisplay, blue3, [640,400],100)
    for i in range(0,8):
        pygame.draw.circle(gameDisplay, muerto[i], [posx[i],posy[i]],radio)
        gameDisplay.blit(posiblesFont.render(str(posibles[i]),1, white),(posx[i]-ajustx,posy[i]-ajusty))
    
    pygame.display.update()    
            
    time.sleep(1)
    
    ## aca va la ruleta
    rand = random.randint(0,7)
    rand8 = rand+8
    rand_6 = rand8/6
    
    
    for i in range(0,rand_6+1):
        for j in range(0,8):
            pygame.draw.circle(gameDisplay, vivo[j], [posx[j],posy[j]],radio)
            gameDisplay.blit(posiblesFont.render(str(posibles[j]),1, white),(posx[j]-ajustx,posy[j]-ajusty))
            
            if j != 0 :
                pygame.draw.circle(gameDisplay, muerto[j-1], [posx[j-1],posy[j-1]],radio)
                gameDisplay.blit(posiblesFont.render(str(posibles[j-1]),1, white),(posx[j-1]-ajustx,posy[j-1]-ajusty))
            else :
                pygame.draw.circle(gameDisplay, muerto[7], [posx[7],posy[7]],radio)
                gameDisplay.blit(posiblesFont.render(str(posibles[7]),1, white),(posx[7]-ajustx,posy[7]-ajusty))
                
            pygame.display.update()
            time.sleep(0.1)
            
    for k in range(0,rand):
        print str(k)
        pygame.draw.circle(gameDisplay, vivo[k], [posx[k],posy[k]],radio)
        gameDisplay.blit(posiblesFont.render(str(posibles[k]),1, white),(posx[k]-ajustx,posy[k]-ajusty))
        if k != 0:
            pygame.draw.circle(gameDisplay, muerto[k-1], [posx[k-1],posy[k  -1]],radio)
            gameDisplay.blit(posiblesFont.render(str(posibles[k-1]),1, white),(posx[k-1]-ajustx,posy[k-1]-ajusty))
        else:
            pygame.draw.circle(gameDisplay, muerto[7], [posx[7],posy[7]],radio)
            gameDisplay.blit(posiblesFont.render(str(posibles[7]),1, white),(posx[7]-ajustx,posy[7]-ajusty))
            
        pygame.display.update()
        time.sleep(0.2)
    
        
    pygame.draw.circle(gameDisplay, vivo[rand-1], [posx[rand-1],posy[rand-1]],radio)
    gameDisplay.blit(posiblesFont.render(str(posibles[rand-1]),1, white),(posx[rand-1]-ajustx,posy[rand-1]-ajusty))
    gameDisplay.blit(ruletaFont.render(str(posibles[rand-1]),1, mangobiche),(545,335))
    pygame.display.update()
    time.sleep(2)

