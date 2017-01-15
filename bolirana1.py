import pygame, random, sys, time
import RPi.GPIO as GPIO
from pygame.locals import *

#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)#MONEDERO
GPIO.setup(10,GPIO.IN)#SELECTOR
GPIO.setup(12,GPIO.IN)#ACEPTAR
GPIO.setup(16,GPIO.IN)#RANA GRANDE
GPIO.setup(18,GPIO.IN)#RANA PEQUENA
GPIO.setup(22,GPIO.IN)#BOTELLA IZQ
GPIO.setup(24,GPIO.IN)#BOTELLA DER
GPIO.setup(26,GPIO.IN)#20 IZQ
GPIO.setup(32,GPIO.IN)#20 DER
GPIO.setup(36,GPIO.IN)#30 IZQ
GPIO.setup(38,GPIO.IN)#30 DER
GPIO.setup(40,GPIO.IN)#40 IZQ
GPIO.setup(37,GPIO.IN)#40 DER
GPIO.setup(35,GPIO.IN)#35 IZQ
GPIO.setup(33,GPIO.IN)#35 DER
GPIO.setup(31,GPIO.IN)#55 IZQ
GPIO.setup(29,GPIO.IN)#55 DER


def ruleta():
    posibles = [250,300,350,400,450,500]
    ## aca va la ruleta
    rand = random.randint(0,5)
    rand8 = rand+8
    rand_6 = rand8/6
    j=0
    print rand
    print rand8
    print rand_6
    for i in range(0,rand_6+1):
        for j in range(0,6):
            print posibles[j]
            time.sleep(0.2)
    for i in range(0,rand):
        print posibles[i]
        j=j+1
        time.sleep(0.2)

    return posibles[rand-1]
        

def puntos ():
    if GPIO.input(16)==0:
        return ruleta()
    elif GPIO.input(18)==0:
        return 200
    elif GPIO.input(22)==0:
        return 100
    elif GPIO.input(24)==0:
        return 100
    elif GPIO.input(26)==0:
        return 20
    elif GPIO.input(32)==0:
        return 20
    elif GPIO.input(36)==0:
        return 30
    elif GPIO.input(38)==0:
        return 30
    elif GPIO.input(40)==0:
        return 40
    elif GPIO.input(37)==0:
        return 40
    elif GPIO.input(35)==0:
        return 35
    elif GPIO.input(33)==0:
        return 35
    elif GPIO.input(31)==0:
        return 55
    elif GPIO.input(29)==0:
        return 55
    else:
        return 0



    
pygame.init()

pygame.mouse.set_visible(False)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
green1 = (0,71,0)
green2 = (0,180,0)
blue = (0,0,255)
blue1 = (51,51,255)
yellow = (255,255,0)
grey = (200,200,200)
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

### Fuentes y tamanios

jugadorSF= 120
puntosSF = 160
restantesSF = 60
huecosSF = 40
metaSF = 60
turnoJugadorSF = 300
turnoPuntosSF = 200
turnoRestantesSF = 100

jugadorFont = pygame.font.Font(None,jugadorSF)
puntosFont = pygame.font.Font(None,puntosSF)
restantesFont = pygame.font.Font(None,restantesSF)
huecosFont = pygame.font.Font(None,huecosSF)
metaFont = pygame.font.Font(None,metaSF)
turnoJugadorFont = pygame.font.Font(None,turnoJugadorSF)
turnoPuntosFont = pygame.font.Font(None,turnoPuntosSF)
turnoRestantesFont = pygame.font.Font(None,turnoRestantesSF)



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
    
boxMarginW = 20
boxMarginH = 50
boxMarginHMapa = 50
boxPad = 80
boxW = 320          
boxH = 220
boxB= 4
numberPadX = 70
padRestantesJugador = 30
padJugadorPuntos = -50



### informacion de jugadores

nJugadores = 5
maxJugadores = 8

### decide si se dejan posiciones vacias o se llenan
### asi los jugadores no esten activos
conVacio = True

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
colorNoActivo = green2 
colorActivo = white
colorBorde = white

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
rExterno1=84
rExterno2=rExterno1/2
rRelleno1=82
rRelleno2=rRelleno1/2

######### Configuracion de la pantalla
gameDisplay=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('Boliranas El Original')

def text_objects (text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def esperando_inicio ():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if GPIO.input(8) == 0:
           menu()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Bolirana", largeText, black)
        TextRect.center = ((screenW/2),(screenH/2))
        gameDisplay.blit(TextSurf,TextRect)

        gameDisplay.blit(huecosFont.render("Insertar",1, black),(100,100))
        pygame.display.update()

def menu ():
    mononaSF = 60
    mononaFont = pygame.font.Font(None,mononaSF)

    labelSF = 100
    labelFont = pygame.font.Font(None,labelSF)

    colorB = yellow
    colorNu = green2
    colorMo = blue
    colorMe = blue
    colorCa = blue
    colorAc = grey69

    colorTi = red

    numero = 1
    mononas = [[" 1 Rana y ",
                "2 Botellas"],
               ["2 Ranas y",
                "1 Botella"],
               [" 2 Ranas y",
                "2 Botellas"]]
    monona = mononas[0]
    metas = 2000
    ca = 0
    i=0
    mo=0
    k=0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if GPIO.input(10)==0:
            if colorNu == green2:
                colorNu=blue
                colorMo=green2
                colorMe=blue
                colorCa=blue
                colorAc=grey69
            elif colorMo == green2:
                colorNu=blue
                colorMo=blue
                colorMe=green2
                colorCa=blue
                colorAc=grey69
            elif colorMe == green2:
                colorNu=blue
                colorMo=blue
                colorMe=blue
                colorCa=green2
                colorAc=grey69
            elif colorCa == green2:
                colorNu=blue
                colorMo=blue
                colorMe=blue
                colorCa=blue
                colorAc=green2
                
            elif colorAc == green2:
                colorNu=green2
                colorMo=blue
                colorMe=blue
                colorCa=blue
                colorAc=grey69

        
        if GPIO.input(8)==0:
            if colorNu== green2:
                numero=numero+1
                if numero>8:
                    numero = 1
            elif colorMo == green2:
                monona = mononas[mo]
                mo=mo+1
                if mo>2:
                    mo=0
            elif colorMe == green2:
                metas = metas+200
                i=i+1
                if metas>5000:
                    i=0
                    metas=2000
            elif colorCa == green2:
                ca=ca+10
                if ca>100:
                    ca=0
            elif colorAc == green2:
                juego(numero, monona, metas, ca)
           
        gameDisplay.fill(blue)

        pygame.draw.rect(gameDisplay, colorB, [248,108,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [250,110,220,100],0)
        gameDisplay.blit(mononaFont.render("Numero de",1, white),(270-2*len("Numero de"),115))
        gameDisplay.blit(mononaFont.render("jugadores",1, white),(270-1*len("jugadores"),155))

        pygame.draw.rect(gameDisplay, colorB, [648,108,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorNu, [650,110,220,100],0)
        gameDisplay.blit(labelFont.render(str(numero),1, white),(750-10*len(str(numero)),130))
        
        pygame.draw.rect(gameDisplay, colorB, [248,248,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [250,250,220,100],0)
        gameDisplay.blit(mononaFont.render("Monona",1, white),(350-12*len("Monona"),280))

        pygame.draw.rect(gameDisplay, colorB, [648,248,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorMo, [650,250,220,100],0)
        gameDisplay.blit(mononaFont.render(str(monona[0]),1, white),(755-9*len(str(monona[0])),260))
        gameDisplay.blit(mononaFont.render(str(monona[1]),1, white),(755-9*len(str(monona[1])),300))

        
        pygame.draw.rect(gameDisplay, colorB, [248,398,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [250,400,220,100],0)
        gameDisplay.blit(mononaFont.render("Meta",1, white),(310,430))

        pygame.draw.rect(gameDisplay, colorB, [648,398,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorMe, [650,400,220,100],0)
        gameDisplay.blit(labelFont.render(str(metas),1, white),(685,410))
   

        pygame.draw.rect(gameDisplay, colorB, [248,548,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [250,550,220,100],0)
        gameDisplay.blit(mononaFont.render("Castigo",1, white),(280,580))

        pygame.draw.rect(gameDisplay, colorB, [648,548,224,104],boxB)
        pygame.draw.rect(gameDisplay, colorCa, [650,550,220,100],0)
        gameDisplay.blit(labelFont.render(str(ca),1, white),(750,560))

        pygame.draw.rect(gameDisplay, colorB, [898,798,184,94],boxB)
        pygame.draw.rect(gameDisplay, colorAc, [900,800,180,90],0)
        
        pygame.display.update()
     
        
        
def h_label(texto):
    largeText = pygame.font.Font('freesansbold.ttf', huecosSF)
    TextSurf, TextRect = text_objects(texto, largeText,white)
    TextRect.center = ((screenW/2),(screenH/2))
    gameDisplay.blit(TextSurf,TextRect)

def h_mapa (x,y):

    ### Mapa de la rana
    ex = -42
    ey = -20
    colorExterno = grey
    colorRelleno = black

    gameDisplay.blit(pygame.image.load('hmapa.png'),(boxW+boxMarginW-2,boxMarginH))

    gameDisplay.blit(pygame.image.load('ranaGrande.png'),(729+x,40+y))
    pygame.draw.ellipse(gameDisplay, colorExterno, [750+x+ex,130+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [750+x+ex,130+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(pygame.image.load('estrella.png'),(710+x,90+y)) 

    gameDisplay.blit(pygame.image.load('ranaPeque.png'),(732+x,180+y))
    pygame.draw.ellipse(gameDisplay, colorExterno, [750+x+ex,250+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [750+x+ex,250+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(hRanaPeque),1, white),(727+x,235+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [840+x+ex,160+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [840+x+ex,160+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h20),1, white),(825+x,145+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [660+x+ex,160+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [660+x+ex,160+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h20),1, white),(645+x,145+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [840+x+ex,280+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [840+x+ex,280+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h30),1, white),(825+x,265+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [660+x+ex,280+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [660+x+ex,280+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h30),1, white),(645+x,265+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [840+x+ex,400+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [840+x+ex,400+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h40),1, white),(825+x,385+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [660+x+ex,400+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [660+x+ex,400+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h40),1, white),(645+x,385+y))

    gameDisplay.blit(pygame.image.load('botella.png'),(915+x,110+y))
    pygame.draw.ellipse(gameDisplay, colorExterno, [930+x+ex,190+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [930+x+ex,190+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(hBotella),1, white),(907+x,175+y))

    gameDisplay.blit(pygame.image.load('botella.png'),(555+x,110+y))
    pygame.draw.ellipse(gameDisplay, colorExterno, [570+x+ex,190+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [570+x+ex,190+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(hBotella),1, white),(547+x,175+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [930+x+ex,310+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [930+x+ex,310+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h35),1, white),(915+x,295+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [570+x+ex,310+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [570+x+ex,310+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h35),1, white),(555+x,295+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [930+x+ex,430+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [930+x+ex,430+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h55),1, white),(915+x,415+y))

    pygame.draw.ellipse(gameDisplay, colorExterno, [570+x+ex,430+y+ey,rExterno1,rExterno2],0)
    pygame.draw.ellipse(gameDisplay, colorRelleno, [570+x+ex,430+y+ey,rRelleno1,rRelleno2],0)
    gameDisplay.blit(huecosFont.render(str(h55),1, white),(555+x,415+y))


def i_mapa(mo, me, ca):
    posXb = boxW+boxMarginW
    
    #pygame.draw.rect(gameDisplay, red, [posXb,500+boxMarginHMapa+10,500,100],0)
    #pygame.draw.rect(gameDisplay, white, [posXb,500+boxMarginHMapa+10,500,100],boxB)
    gameDisplay.blit(pygame.image.load('box.png'),(boxW+boxMarginW,500+boxMarginHMapa))

    gameDisplay.blit(huecosFont.render("MONONA",1, red),(posXb+35,500+boxMarginHMapa+15))
    gameDisplay.blit(huecosFont.render(mo[0],1, yellow),(posXb +50-(2*len(str(mo[0]))),500+boxMarginHMapa+45))
    gameDisplay.blit(huecosFont.render(mo[1],1, yellow),(posXb +50-(2*len(str(mo[1]))),500+boxMarginHMapa+70))

    gameDisplay.blit(pygame.image.load('box.png'),(posXb +200,500+boxMarginHMapa))
    gameDisplay.blit(huecosFont.render("META",1, red),(posXb+265,500+boxMarginHMapa+15))
    gameDisplay.blit(metaFont.render(str(me),1, yellow),(posXb+255,500+boxMarginHMapa+55))

    gameDisplay.blit(pygame.image.load('box.png'),(posXb +400,500+boxMarginHMapa))
    gameDisplay.blit(huecosFont.render("CASTIGO",1, red),(posXb+440,500+boxMarginHMapa+15))
    gameDisplay.blit(huecosFont.render("-"+str(ca),1, yellow),(posXb+480,500+boxMarginHMapa+65))

def t_mapa(turno):
    gameDisplay.blit(turnoJugadorFont.render(str(jugadores[turno]),1, yellow),(screenW/2-200,660))

    gameDisplay.blit(turnoPuntosFont.render(str(puntos[turno]),1, yellow),(screenW/2-50+100,680))

    gameDisplay.blit(turnoRestantesFont.render(str(restantes[turno]),1,yellow),(screenW/2-50+100,820))


def p_mapa(nu):
    
    ### Sistema de puntaje
        for i in range(0,nu):
            if activos[i] == 1:
                color = colorActivo
            else:
                color = colorNoActivo

            gameDisplay.blit(pygame.image.load('turnoOFF.png'),(posx[i],posy[i]))            
            #pygame.draw.rect(gameDisplay, colorBorde, [posx[i],posy[i],boxW,boxH],boxB)
            
            puntosl = puntosFont.render(str(puntos[i]),1, color)
            gameDisplay.blit(puntosl,(posx[i]+boxW/2-(30*len(str(puntos[i]))),posy[i]+puntosSF+padJugadorPuntos))
            
            restantesl = restantesFont.render(str(restantes[i]),1, color)
            gameDisplay.blit(restantesl,(posx[i]+boxW-(30*len(str(restantes[i]))),posy[i]+5))
            
            jugadorl = jugadorFont.render(str(jugadores[i]),1, color)
            if jugadores[i] < 10:
                gameDisplay.blit(jugadorl,(posx[i]+boxW/2-(40*len(str(jugadores[i]))),posy[i]+padRestantesJugador))
            else:
                gameDisplay.blit(jugadorl,(posx[i]+boxW/2-(40*len(str(jugadores[i])))+numberPadX-50,posy[i]+padRestantesJugador))

        pygame.display.update()
    

def draw_bolita(id_hueco, cuentas):
    ex=-140
    ey=80
    colorExterno = yellow
    radio = 5
    if id_hueco == 1:
        pygame.draw.circle(gameDisplay, colorExterno, [750+ex+12*cuentas,130+ey],radio)
    elif id_hueco == 2:
        pygame.draw.circle(gameDisplay, colorExterno, [750+ex+12*cuentas,250+ey],radio)
    elif id_hueco == 3:
        pygame.draw.circle(gameDisplay, colorExterno, [840+ex+12*cuentas,160+ey],radio)
    elif id_hueco == 4:
        pygame.draw.circle(gameDisplay, colorExterno, [660+ex+12*cuentas,160+ey],radio)
    elif id_hueco == 5:
        pygame.draw.circle(gameDisplay, colorExterno, [840+ex+12*cuentas,280+ey],radio)
    elif id_hueco == 6:
        pygame.draw.circle(gameDisplay, colorExterno, [660+ex+12*cuentas,280+ey],radio)
    elif id_hueco == 7:
        pygame.draw.circle(gameDisplay, colorExterno, [840+ex+12*cuentas,400+ey],radio)
    elif id_hueco == 8:
        pygame.draw.circle(gameDisplay, colorExterno, [660+ex+12*cuentas,400+ey],radio)
    elif id_hueco == 9:
        pygame.draw.circle(gameDisplay, colorExterno, [930+ex+12*cuentas,190+ey],radio)
    elif id_hueco == 10:
        pygame.draw.circle(gameDisplay, colorExterno, [570+ex+12*cuentas,190+ey],radio)
    elif id_hueco == 11:
        pygame.draw.circle(gameDisplay, colorExterno, [930+ex+12*cuentas,310+ey],radio)
    elif id_hueco == 12:
        pygame.draw.circle(gameDisplay, colorExterno, [570+ex+12*cuentas,310+ey],radio)
    elif id_hueco == 13:
        pygame.draw.circle(gameDisplay, colorExterno, [930+ex+12*cuentas,430+ey],radio)
    elif id_hueco == 14:
        pygame.draw.circle(gameDisplay, colorExterno, [570+ex+12*cuentas,430+ey],radio)
    pygame.display.update()
        
def juego(nu, mo, me, ca):

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.blit(pygame.image.load('background1.png'),(0,0))
            

        h_mapa(-110,boxMarginHMapa-10)
        i_mapa(mo, me, ca)
        t_mapa(0)
        p_mapa(nu)
        draw_bolita(5,2)

        
    
##### Inicio
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    esperando_inicio()   
    
pygame.quit()
quit()
