#Esta es la pruenba de un juego generico para empezar a comstruir la bolirana
import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1024, 768), 0 , 32)

backgroundfile = "background1.jpeg"
mousefile = "rana3.png"

background = pygame.image.load(backgroundfile).convert()
mouse = pygame.image.load(mousefile).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys,exit()

    #Ahora tenemo todo inicializado

    screen.blit(background, (0,0))

    x,y = pygame.mouse.get_pos()

    x -= mouse.get_width()/2
    y -= mouse.get_height()/2

    screen.blit(mouse, (x,y))

    pygame.display.update()
    
