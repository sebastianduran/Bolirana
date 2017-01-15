# -*- coding: iso-8859-15 -*-
import pygame, random, sys, time, os, subprocess, glob
import RPi.GPIO as GPIO
from pygame.locals import *

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#reload(sys)
#sys.setdefaultencoding('ISO885915')

pclientes ="   Finca El Encanto"
celOriginal = "314 5078205 - 310 8101693"
#set GPIO numbering mode and define input pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)#MONEDERO
GPIO.setup(10,GPIO.IN)#SELECTOR
GPIO.setup(12,GPIO.IN)#ACEPTAR
GPIO.setup(16,GPIO.IN)# RANA GRANDE      h1
GPIO.setup(18,GPIO.IN)#RANA PEQUENA     h2
GPIO.setup(22,GPIO.IN)#BOTELLA IZQ      h3
GPIO.setup(24,GPIO.IN)#BOTELLA DER      h4
GPIO.setup(26,GPIO.IN)#20 IZQ           h5
GPIO.setup(32,GPIO.IN)#20 DER           h6
GPIO.setup(36,GPIO.IN)#30 IZQ           h7
GPIO.setup(38,GPIO.IN)#30 DER           h8
GPIO.setup(40,GPIO.IN)#40 IZQ           h9
GPIO.setup(37,GPIO.IN)#40 DER           h10
GPIO.setup(35,GPIO.IN)#35 IZQ           h11
GPIO.setup(33,GPIO.IN)#35 DER           h12
GPIO.setup(31,GPIO.IN)#55 IZQ           h13
GPIO.setup(29,GPIO.IN)#55 DER           h14


##os.system("omxplayer -o hdmi /home/pi/bolirana/videos/video4.mp4")
##video=subprocess.Popen(['omxplayer', '--win','\350,200,20,20\'','/home/pi/bolirana/videos/video3.mp4'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)

pygame.init()

pygame.mouse.set_visible(False)
#pygame.display.set_mode((1280,1024),FULLSCREEN)

#colores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
green1 = (0,71,0)
green2 = (0,180,0)
greenlime = (156,255,0)
blue = (0,0,255)
blue1 = (51,51,255)
yellow = (255,255,0)
grey = (200,200,200)
grey22 = (56,56,56)
grey69 = (176,176,176)
orange1 = (255,69,0)
chocolate = (205,150,30)
mango = (168,146,0)
indigo = (75,0,130)
greendark=(0,128,0)
bluedark=(0,0,128)
reddark=(128,0,0)
magentadark=(128,0,128)
magenta=(255,0,255)
blue2=(0,90,255)
orange2 = (255,195,0)
magenta2=(255,0,90)
mangobiche=(255,255,51)
blue3=(26,0,179)

maxJugadores = 8

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
boliranaFont = pygame.font.Font('caterine.ttf',85)
barFont = pygame.font.Font('teamspirs.ttf', 90)
infoFont = pygame.font.Font(None, 32)

####################################

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


### dimesiones circulos
rExterno1=84
rExterno2=rExterno1/2
rRelleno1=82
rRelleno2=rRelleno1/2

######### Configuracion de la pantalla
gameDisplay=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption('El Original')

def text_objects (text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def esperando_inicio ():
    #os.system('videoplayer.sh'+'/home/pi/bolirana/videos')
    #subprocess.Popen(['./videoplayer.sh', "var=11; ignore=all", '/home/pi/bolirana/videos'],shell=True,executable="/bin/bash")
    subprocess.Popen(['bash', '/home/pi/bolirana/videos/videoplayer.sh'])
    i=0
    j=0
    colorBack = orange2
    colorText = blue
    
    while True:
        #print str(GPIO.input(8))
        if GPIO.input(8) == 0:
            subprocess.Popen(["pkill", "bash"])
            subprocess.Popen(["pkill", "omxplayer.bin"])
            subprocess.Popen(["pkill", "omxplayer"])
            menu()

##        else:
##            if colorBack == orange1:
##                i=i+1
##                if i > 1000:
##                    colorBack = yellow
##                    i=0
##            else:
##                i=i+1
##                if i > 1000:
##                    colorBack = orange1
##                    i=0
##
            if colorText == blue:
                j=j+1
                if j > 70:
                    colorText = black
                    j=0
            else:
                j=j+1
                if j > 70:
                    colorText = blue
                    j=0


        gameDisplay.fill(colorBack)
        
        gameDisplay.blit(boliranaFont.render("El Original",1, colorText),(400,-20))
        gameDisplay.blit(infoFont.render("Punto de fabrica",1, colorText),(650,20))
        gameDisplay.blit(infoFont.render(celOriginal,1, colorText),(850,20))
        gameDisplay.blit(barFont.render(pclientes,1, colorText),(150,880))
        pygame.display.update()

def menu ():
    mononaSF = 60
    mononaFont = pygame.font.Font(None,mononaSF)

    labelSF = 100
    labelFont = pygame.font.Font(None,labelSF)

    colorB = black
    colorNu = green2
    colorMo = blue
    colorMe = blue
    colorCa = blue
    colorAc = white

    colorTi = red

    numero = 2
    mononas = [["   Sin    ", "  Moñona  ", "1"],
               [" 1 Rana y ", "2 Botellas", "2"],
               ["2 Ranas y ", "1 Botella ", "3"],
               [" 2 Ranas y", "2 Botellas", "4"]]
    monona = mononas[0]
    metas = 2000
    ca = 0
    i=0
    mo=0
    k=0

    gameDisplay.blit(pygame.image.load('background110.jpg'),(0,0))
    menuExit = False
    while not menuExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if GPIO.input(10)==1:
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
                
            time.sleep(0.3)
        
        if GPIO.input(12)==0:
            if colorNu== green2:
                numero=numero+1
                if numero>8:
                    numero = 2
            elif colorMo == green2:
                mo=mo+1
                if mo>3:
                    mo=0
                monona = mononas[mo]
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
                menuExit=juego(numero, monona, metas, ca)

            time.sleep(0.3)
  

        #pygame.draw.rect(gameDisplay, colorB, [198,108,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [200,110,320,100],0)
        gameDisplay.blit(mononaFont.render("Numero de",1, white),(270-2*len("Numero de"),115))
        gameDisplay.blit(mononaFont.render("jugadores",1, white),(270-1*len("jugadores"),155))

        #pygame.draw.rect(gameDisplay, colorB, [598,108,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorNu, [600,110,320,100],0)
        gameDisplay.blit(labelFont.render(str(numero),1, white),(750-10*len(str(numero)),130))
        
        #pygame.draw.rect(gameDisplay, colorB, [198,248,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [200,250,320,100],0)
        gameDisplay.blit(mononaFont.render("Moñona",1, white),(350-12*len("Monona"),280))

        #pygame.draw.rect(gameDisplay, colorB, [598,248,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorMo, [600,250,320,100],0)
        gameDisplay.blit(mononaFont.render(str(monona[0]),1, white),(755-9*len(str(monona[0])),260))
        gameDisplay.blit(mononaFont.render(str(monona[1]),1, white),(755-9*len(str(monona[1])),300))

        
        #pygame.draw.rect(gameDisplay, colorB, [198,398,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [200,400,320,100],0)
        gameDisplay.blit(mononaFont.render("Meta",1, white),(310,430))

        #pygame.draw.rect(gameDisplay, colorB, [598,398,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorMe, [600,400,320,100],0)
        gameDisplay.blit(labelFont.render(str(metas),1, white),(685,410))
   

        #pygame.draw.rect(gameDisplay, colorB, [198,548,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorTi, [200,550,320,100],0)
        gameDisplay.blit(mononaFont.render("Castigo",1, white),(280,580))

        #pygame.draw.rect(gameDisplay, colorB, [598,548,324,104],boxB)
        pygame.draw.rect(gameDisplay, colorCa, [600,550,320,100],0)
        gameDisplay.blit(labelFont.render(str(ca),1, white),(755-11*len(str(ca)),560))

        #pygame.draw.rect(gameDisplay, colorB, [898,798,184,94],boxB)
        pygame.draw.rect(gameDisplay, colorAc, [900,800,180,90],0)
        gameDisplay.blit(mononaFont.render("Aceptar",1, black),(910,820))

        pygame.display.update()
        

def publicidad ():
    gameDisplay.blit(boliranaFont.render("El Original",1, white),(500,-10))
    gameDisplay.blit(infoFont.render("Punto de fabrica",1, white),(820,20))
    gameDisplay.blit(infoFont.render(celOriginal,1, black),(960,20))
    gameDisplay.blit(huecosFont.render(pclientes,1, black),(450,900))
    
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

    gameDisplay.blit(pygame.image.load('hmapa.png'),(boxW+boxMarginW-0.5,boxMarginH))

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

    gameDisplay.blit(huecosFont.render("MOÑONA",1, red),(posXb+35,500+boxMarginHMapa+15))
    gameDisplay.blit(huecosFont.render(mo[0],1, yellow),(posXb +50-(2*len(str(mo[0]))),500+boxMarginHMapa+45))
    gameDisplay.blit(huecosFont.render(mo[1],1, yellow),(posXb +50-(2*len(str(mo[1]))),500+boxMarginHMapa+70))

    gameDisplay.blit(pygame.image.load('box.png'),(posXb +200,500+boxMarginHMapa))
    gameDisplay.blit(huecosFont.render("META",1, red),(posXb+265,500+boxMarginHMapa+15))
    gameDisplay.blit(metaFont.render(str(me),1, yellow),(posXb+255,500+boxMarginHMapa+55))

    gameDisplay.blit(pygame.image.load('box.png'),(posXb +400,500+boxMarginHMapa))
    gameDisplay.blit(huecosFont.render("CASTIGO",1, red),(posXb+440,500+boxMarginHMapa+15))
    gameDisplay.blit(huecosFont.render("-"+str(ca),1, yellow),(posXb+480,500+boxMarginHMapa+65))

def t_mapa(turno,puntos,restantes):
    
    gameDisplay.blit(pygame.image.load('fondopuntaje.png'),(350,665))
    
    gameDisplay.blit(turnoJugadorFont.render(str(turno),1, red),(screenW/2-180,660))

    gameDisplay.blit(turnoPuntosFont.render(str(puntos),1, red),(660-20*len(str(puntos)),680))

    gameDisplay.blit(turnoRestantesFont.render(str(restantes),1,red),(680-5*len(str(restantes)),820))


def p_mapa(n,turno,jugadores, puntos, restantes,activos):
    n_2 = n/2
    m=maxJugadores
    m_2 = maxJugadores/2
    x=0
    ### nombre del jugador, puntos y restantes
    colorNoActivo = mango
    colorActivo = white
    colorBorde = white
    
    ##posiciones
    posx = list(range(m))
    j=0
    for k in range (0, m_2+x):
        posx[k]= boxMarginW
        j=j+1
    j=0
    for k in range (m_2+x, m):
        posx[k]= screenW-boxW-boxMarginW
        j=j+1
        
    posy = list(range(m))
    j=0
    for i in range(0,m_2+x):
        posy[i]= (boxH*j)+boxMarginH
        j=j+1
    j=0
    for i in range(m_2+x,m):
        posy[i]= (boxH*j)+boxMarginH
        j=j+1
    
    ### Sistema de puntaje
    for i in range(0,m):
        if activos[i] == 1:
            color = colorActivo
        else:
            color = colorNoActivo

        t=turno-1
        gameDisplay.blit(pygame.image.load('turnoOFF.png'),(posx[i],posy[i]))
        if i == t :
            gameDisplay.blit(pygame.image.load('turnoON.png'),(posx[i],posy[i]))

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

    
def ruleta():
    #gameDisplay.blit(pygame.image.load('ruleta.png'),(415,250))
    pygame.mixer.music.load("ruleta3.mp3")
    pygame.mixer.music.play()
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

    ruletaFont = pygame.font.Font(None,200)
    posiblesFont= pygame.font.Font(None,80)

    radio=65
    ajustx=48
    ajusty=30

    gameDisplay.blit(pygame.image.load('ruletapic.png'),(370,129))               
    #pygame.draw.circle(gameDisplay, orange2, [640,400],250)
    #pygame.draw.circle(gameDisplay, blue3, [640,400],100)
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
            time.sleep(0.08)
            
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
        time.sleep(0.15)
        
            
    pygame.draw.circle(gameDisplay, vivo[rand-1], [posx[rand-1],posy[rand-1]],radio)
    gameDisplay.blit(posiblesFont.render(str(posibles[rand-1]),1, white),(posx[rand-1]-ajustx,posy[rand-1]-ajusty))
    pygame.draw.circle(gameDisplay, yellow, [640,400],125)
    gameDisplay.blit(ruletaFont.render(str(posibles[rand-1]),1, reddark),(525,320))
    pygame.display.update()
    time.sleep(1)

    return posibles[rand-1]
        

def encholada():
    ON = 0
    ONON = 0
    if GPIO.input(16)==ON:
        return [ruleta(), 1]
    elif GPIO.input(18)==ON:
        pygame.mixer.music.load("ranapeque.mp3")
        pygame.mixer.music.play()
        return [200, 2]
    elif GPIO.input(22)==ON:
        pygame.mixer.music.load("botella.mp3")
        pygame.mixer.music.play()
        return [100, 3]
    elif GPIO.input(24)==ON:
        pygame.mixer.music.load("botella.mp3")
        pygame.mixer.music.play()
        return [100, 4]
    elif GPIO.input(26)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [20, 5]
    elif GPIO.input(32)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [20, 6]
    elif GPIO.input(36)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [30, 7]
    elif GPIO.input(38)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [30, 8]
    elif GPIO.input(40)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [40, 9]
    elif GPIO.input(37)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [40, 10]
    elif GPIO.input(35)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [35, 11]
    elif GPIO.input(33)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [35, 12]
    elif GPIO.input(31)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [55, 13]
    elif GPIO.input(29)==ON:
        pygame.mixer.music.load("espada.wav")
        pygame.mixer.music.play()
        return [55, 14]
    else:
        return [0,0]

def draw_bolita(huecos):  
    ex=-140
    ey=80
    colorExterno = yellow
    radio = 5
    
    pox = [750+ex,750+ex,570+ex,930+ex,660+ex,840+ex,660+ex,840+ex,660+ex,840+ex,570+ex,930+ex,570+ex,930+ex]
    poy = [130+ey,250+ey,190+ey,190+ey,160+ey,160+ey,280+ey,280+ey,400+ey,400+ey,310+ey,310+ey,430+ey,430+ey]
    ##PASAR A DICIONARIOS LO QUE MAS SE PUEDA
    for id_ in range(0,len(huecos)):
        for cuentas in range(0,huecos[id_]):
            pygame.draw.circle(gameDisplay, colorExterno, [pox[id_]+12*cuentas,poy[id_]],radio)       


    
def juego(n, mo, me, ca):
    pygame.mixer.music.load("introjuego.mp3")
    pygame.mixer.music.play()
    turno = 1
    vacio = 0
    
    restantesT = me
    m=maxJugadores
    m_2 = maxJugadores/2

    monoDic = {"1": [10000,10000],"2": [1,2],"3": [2,1],"4":[2,2]}
    monoTur = [0,0]

    jugadores = list(range(m))
    for i in range(0,m):
        jugadores[i]= str(i+1)

    puntos = list(range(m))
    for i in range(0,m):      
        puntos[i]=0
        
    restantes = list(range(m))
    for i in range(0,m):
        restantes[i]=me

    activos = list(range(m))
    for i in range(0,n):
        activos[i]=1
    for i in range(n,m):
        activos[i]=0
    
    gameExit = False
    huecosC=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]##para llevar las cuentas en el huecos encholados
    jview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
    pygame.display.update()
    
    while not gameExit:
        ###for event in pygame.event.get():
        ###     if event.type == pygame.QUIT:
        ###        gameExit = True
       
        puntosT=0
        cuentas = 0
        ### decide si se dejan posiciones vacias o se llenan
        ### asi los jugadores no esten activos]##
        while GPIO.input(10)==0 and puntosT <13:

            valor = encholada()
            
            if valor[0]>0:
                puntos[turno-1] = puntos[turno-1] + valor[0]
                
                if valor[0]>1:
                    if valor[0]>=300:
                        monoTur[0]=monoTur[0]+1
                        puntosT=puntosT+1
                        jview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
                    elif valor[0]==200:
                        monoTur[0]=monoTur[0]+1
                        puntosT=puntosT+1
                    elif valor[0]==100:
                        monoTur[1]=monoTur[1]+1
                        puntosT=puntosT+1
                    elif valor[0] >= 20:
                        puntosT=puntosT+1
                       
                    huecosC[valor[1]-1] = huecosC[valor[1]-1] +1
                    restantes[turno-1] = me - puntos[turno-1]
                    
                    #pview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
                    #draw_bolita(huecosC)
                    #pygame.display.update()
##                    count = 0
##                    while count < 10:
##                        
##                        count = count + 1
##                        #time.sleep(0.016)     
##                        valor1 = encholada()
##                        if valor1[0]>0:
##                            puntos[turno-1] = puntos[turno-1] + valor1[0]
##                        
##                            if valor1[0]>=300:
##                                monoTur[0]=monoTur[0]+1
##                                puntosT=puntosT+1
##                            elif valor1[0]==200:
##                                monoTur[0]=monoTur[0]+1
##                                puntosT=puntosT+1
##                            elif valor1[0]==100:
##                                monoTur[1]=monoTur[1]+1
##                                puntosT=puntosT+1
##                            elif valor1[0] >= 20:
##                                puntosT=puntosT+1
##                               
##                            huecosC[valor1[1]-1] = huecosC[valor1[1]-1] +1
##                            restantes[turno-1] = me - puntos[turno-1] 

                    draw_bolita(huecosC)
                    pview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
                    draw_bolita(huecosC)
                    pygame.display.update()


                if restantes[turno-1] <= 0 and activos[turno-1]==1:
                    activos[turno-1]=0
                    gano = ganador (turno)
                    break

                if monoDic[mo[2]][0]<=monoTur[0] and monoDic[mo[2]][1]<=monoTur[1] and activos[turno-1]==1:
                    activos[turno-1]=0
                    monoTur = [0,0]
                    gano = ganador (turno)
                    break
                
        if puntosT < 1:
            #if puntos[turno-1] > 0:
            puntos[turno-1]=puntos[turno-1] -ca           
            restantes[turno-1] = restantes[turno-1]+ca
            jview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
            pygame.display.update()
                               

        turno=turno+1
        if turno > n:
            turno = 1
        while activos[turno-1]==0:
            turno=turno+1
            if turno > n:
                turno = 1
        
        
        jview(n, mo, me, ca, turno, puntos, jugadores,restantes, activos)
        pygame.display.update()
        huecosC=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        aux=0
        tr=0
        for i in range(0,len(activos)):
                aux=aux+activos[i]
                if activos[i] == 1:
                    tr=i+1
        if aux == 1:
            fin_juego(tr)

    return True
                
def pview(n, mo, me, ca, turno,puntos,jugadores, restantes, activos):
    #gameDisplay.blit(pygame.image.load('background1.png'),(0,0))

    #h_mapa(-110,boxMarginHMapa-10)
    i_mapa(mo, me, ca)
    t_mapa(turno,puntos[turno-1],restantes[turno-1])
    p_mapa(n,turno,jugadores, puntos, restantes,activos)
    publicidad ()

def jview(n, mo, me, ca, turno,puntos,jugadores, restantes, activos):
    gameDisplay.blit(pygame.image.load('background1.png'),(0,0))

    h_mapa(-110,boxMarginHMapa-10)
    i_mapa(mo, me, ca)
    t_mapa(turno,puntos[turno-1],restantes[turno-1])
    p_mapa(n,turno,jugadores, puntos, restantes,activos)
    publicidad ()
        
def fin_juego (turno):
    pygame.mixer.music.load("fail.mp3")
    pygame.mixer.music.play()
    mononaSF = 60
    mononaFont = pygame.font.Font(None,mononaSF)
    

    #pygame.draw.rect(gameDisplay, red, [200,200,860,500],0)
    pygame.draw.ellipse(gameDisplay, red, [200,200,900,500],0)
    
    gameDisplay.blit(puntosFont.render(" Fin del juego ",1, yellow),(260,305))
    gameDisplay.blit(puntosFont.render("   Jugador "+str(turno),1, yellow),(300,505))
    pygame.display.update()
    time.sleep(7)
    esperando_inicio()
        
def ganador (turno):
    pygame.mixer.music.load("gano2.mp3")
    pygame.mixer.music.play()
    mononaSF = 60
    mononaFont = pygame.font.Font(None,mononaSF)

    #pygame.draw.rect(gameDisplay, blue, [200,200,860,500],0)
    pygame.draw.ellipse(gameDisplay, blue, [200,200,900,500],0)
        
    gameDisplay.blit(puntosFont.render("Meta cumplida",1, yellow),(260,305))
    gameDisplay.blit(puntosFont.render("   Jugador "+str(turno),1, yellow),(300,505))
    pygame.display.update()
    time.sleep(5)
    #pygame.mixer.music.stop()
    return True

        
##### Inicio
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    esperando_inicio()   
    
pygame.quit()
quit()
