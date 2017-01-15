import pygame, random, sys
from pygame.locals import *

pygame.init()

pygame.mouse.set_visible(False)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey22 = (56,56,56)
grey69 = (176,176,176)

### resolucion de pantalla

screenW=1280
screenH=1000

### Puntajes de los huecos

hRana = 300
hRanaPeque = 200
h20 = 20
h30 = 30
h40 = 40
hBotella = 100
h35 = 35
h55 = 55

### Tamano letra (Size Font)

jugadorSF= 120
puntosSF = 80
restantesSF = 30
huecosSF = 40
metaSF = 60

### configuracion del juego

meta = 2000
castigo = 10

### informacion de jugadores

nJugadores = 5
maxJugadores = 8
jugadores = list(range(nJugadores))
for i in range(0,nJugadores):
    jugadores[i]= str(i+1)

puntos = list(range(nJugadores))
for i in range(0,nJugadores):
    puntos[i]=0
    
restantes = list(range(nJugadores))
for i in range(0,nJugadores):
    restantes[i]=meta


#cajas de los jugadores
    
boxMarginW = 130
boxMarginH = 20
boxMarginHMapa = 50
boxPad = 80
boxW = 200          
boxH = 150
boxB= 4
numberPadX = 70
padRestantesJugador = 5
padJugadorPuntos = 10



### informacion de jugadores

nJugadores = 5
maxJugadores = 8

### decide si se dejan posiciones vacias o se llenan
### asi los jugadores no esten activos
conVacio = False

if conVacio:
    n = nJugadores
else:
    n = maxJugadores
n_2 = n/2


if (n % 2) == 0:   
    x=0
else:
    x=1
##posicioes    
posx = list(range(n))
j=0
for k in range (0, n_2+x):
    posx[k]= boxMarginW
    j=j+1
j=0
for k in range (n_2+x, n):
    posx[k]= screenW-boxW-boxMarginW
    j=j+1
    
posy = list(range(n))
j=0
for i in range(0,n_2+x):
    posy[i]= (boxH*j)+boxMarginH
    j=j+1
j=0
for i in range(n_2+x,n):
    posy[i]= (boxH*j)+boxMarginH
    j=j+1

### nombre del jugador, puntos y restantes
colorNoActivo = grey69
colorActivo = white

jugadores = list(range(n))
for i in range(0,n):
    jugadores[i]= str(i+1)

puntos = list(range(n))
for i in range(0,n):
    puntos[i]=20
    
restantes = list(range(n))
for i in range(0,n):
    restantes[i]=meta

activos = list(range(n))
for i in range(0,n):
    activos[i]=0
for i in range(0,nJugadores):
    activos[i]=1



### dimesiones circulos
circuloExterno=32
circuloRelleno=30

######### Configuracion de la pantalla
gameDisplay=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('Boliranas El Original')

jugadorFont = pygame.font.Font(None,jugadorSF)
puntosFont = pygame.font.Font(None,puntosSF)
restantesFont = pygame.font.Font(None,restantesSF)
huecosFont = pygame.font.Font(None,huecosSF)
metaFont = pygame.font.Font(None,metaSF)

def text_objects (text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def esperando_inicio ():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    juego()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Bolirana", largeText, black)
        TextRect.center = ((screenW/2),(screenH/2))
        gameDisplay.blit(TextSurf,TextRect)

        gameDisplay.blit(huecosFont.render("Presiona s para iniciar",1, black),(100,100))
        pygame.display.update()
        
def h_label(texto):
    largeText = pygame.font.Font('freesansbold.ttf', huecosSF)
    TextSurf, TextRect = text_objects(texto, largeText,white)
    TextRect.center = ((screenW/2),(screenH/2))
    gameDisplay.blit(TextSurf,TextRect)

def h_mapa (x,y):

    ### Mapa de la rana
    pygame.draw.rect(gameDisplay, white, [500+x,10+y,500,500],boxB)

    gameDisplay.blit(pygame.image.load('rana.png'),(730+x,40+y)) 
    pygame.draw.circle(gameDisplay, white, [750+x,130+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [750+x,130+y], circuloRelleno)
    gameDisplay.blit(pygame.image.load('estrella.png'),(710+x,90+y)) 

    gameDisplay.blit(pygame.image.load('ranapeque.png'),(730+x,180+y))
    pygame.draw.circle(gameDisplay, white, [750+x,250+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [750+x,250+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(hRanaPeque),1, white),(727+x,235+y))

    pygame.draw.circle(gameDisplay, white, [840+x,160+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [840+x,160+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h20),1, white),(825+x,145+y))

    pygame.draw.circle(gameDisplay, white, [660+x,160+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [660+x,160+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h20),1, white),(645+x,145+y))
    
    pygame.draw.circle(gameDisplay, white, [840+x,280+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [840+x,280+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h30),1, white),(825+x,265+y))

    pygame.draw.circle(gameDisplay, white, [660+x,280+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [660+x,280+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h30),1, white),(645+x,265+y))

    pygame.draw.circle(gameDisplay, white, [840+x,400+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [840+x,400+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h40),1, white),(825+x,385+y))

    pygame.draw.circle(gameDisplay, white, [660+x,400+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [660+x,400+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h40),1, white),(645+x,385+y))

    gameDisplay.blit(pygame.image.load('botella.png'),(915+x,110+y))
    pygame.draw.circle(gameDisplay, white, [930+x,190+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [930+x,190+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(hBotella),1, white),(907+x,175+y))

    gameDisplay.blit(pygame.image.load('botella.png'),(555+x,110+y))
    pygame.draw.circle(gameDisplay, white, [570+x,190+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [570+x,190+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(hBotella),1, white),(547+x,175+y))

    pygame.draw.circle(gameDisplay, white, [930+x,310+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [930+x,310+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h35),1, white),(915+x,295+y))

    pygame.draw.circle(gameDisplay, white, [570+x,310+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [570+x,310+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h35),1, white),(555+x,295+y))

    pygame.draw.circle(gameDisplay, white, [930+x,430+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [930+x,430+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h55),1, white),(915+x,415+y))

    pygame.draw.circle(gameDisplay, white, [570+x,430+y], circuloExterno)
    pygame.draw.circle(gameDisplay, black, [570+x,430+y], circuloRelleno)
    gameDisplay.blit(huecosFont.render(str(h55),1, white),(555+x,415+y))


def i_mapa():
    posXb = 500-110
    monona = ["2 Botellas","1 Rana"]
    pygame.draw.rect(gameDisplay, white, [posXb,500+boxMarginHMapa,500,100],boxB)

    gameDisplay.blit(huecosFont.render("MONONA",1, white),(posXb+35,500+boxMarginHMapa+5))
    gameDisplay.blit(huecosFont.render(monona[0],1, white),(posXb+50-(2*len(str(monona[0]))),500+boxMarginHMapa+35))
    gameDisplay.blit(huecosFont.render(monona[1],1, white),(posXb+60-(2*len(str(monona[1]))),500+boxMarginHMapa+60))

    gameDisplay.blit(huecosFont.render("META",1, white),(posXb+215,500+boxMarginHMapa+5))
    gameDisplay.blit(metaFont.render(str(meta),1, white),(posXb+205,500+boxMarginHMapa+45))

    gameDisplay.blit(huecosFont.render("CASTIGO",1, white),(posXb+340,500+boxMarginHMapa+5))
    gameDisplay.blit(huecosFont.render("-"+str(castigo),1, white),(posXb+380,500+boxMarginHMapa+55))



def juego():

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            
        gameDisplay.fill(green)

        h_mapa(-110,boxMarginHMapa-10)
        i_mapa()

        ### Sistema de puntaje
        for i in range(0,n):
            if activos[i] == 1:
                color = colorActivo
            else:
                color = colorNoActivo
            
            pygame.draw.rect(gameDisplay, white, [posx[i],posy[i],boxW,boxH],boxB)
            
            puntosl = puntosFont.render(str(puntos[i]),1, color)
            gameDisplay.blit(puntosl,(posx[i]+boxW/2-(15*len(str(puntos[i]))),posy[i]+puntosSF+padJugadorPuntos))
            
            restantesl = restantesFont.render(str(restantes[i]),1, color)
            gameDisplay.blit(restantesl,(posx[i]+boxW-(15*len(str(restantes[i]))),posy[i]+5))
            
            jugadorl = jugadorFont.render(str(jugadores[i]),1, color)
            if jugadores[i] < 10:
                gameDisplay.blit(jugadorl,(posx[i]+boxW/2-(40*len(str(jugadores[i]))),posy[i]+padRestantesJugador))
            else:
                gameDisplay.blit(jugadorl,(posx[i]+boxW/2-(40*len(str(jugadores[i])))+numberPadX-50,posy[i]+padRestantesJugador))

        pygame.display.update()
    
##### Inicio
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    esperando_inicio()   
    
pygame.quit()
quit()
