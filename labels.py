import sys
import pygame


import cv2
pygame.init()
pygame.mixer.init()


captura = cv2.VideoCapture('youmusic.mp4')



size=(800, 600)
#colores
rojo=[249, 0, 0]
blanco=[255, 255, 255]
negro=[0, 0, 0]
aqua=[0, 255, 255]
plomo=[192, 192, 192]
warning=[240, 173, 78]
rosa=[255, 219, 192]
amarillo=[255, 244, 192]
#OBS
ancho=10
largo=300
x=700
y=400
#Colisiones
px=120
py=300
#el circulo
cx=200
cy=100
radio=80#80
#cuadrado
mx=20
my=200
#pelota
rp=8#14
pex=100
pey=530
p_deltax=0
p_deltay=0
pix=100
piy=530
clok=pygame.time.Clock()

fondo=pygame.image.load('negro.jpeg')


screen= pygame.display.set_mode(size)
screen1=pygame.display.set_mode((800,600))
screen2=pygame.display.set_mode((800,600))


sonido_fondo = pygame.mixer.Sound("miss.wav")
pygame.mixer.Sound.play(sonido_fondo)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key == ord('d'):
                p_deltax=2
            if event.key==pygame.K_LEFT or event.key == ord('a'):
                p_deltax=-2
            if event.key==pygame.K_UP or event.key == ord('w'):
                p_deltay=-2
            if event.key==pygame.K_DOWN or event.key == ord('s'):
                p_deltay=2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                p_deltax = 0
            if event.key==pygame.K_LEFT or event.key == ord('a'):
                p_deltax=0
            if event.key==pygame.K_UP or event.key == ord('w'):
                p_deltay=0
            if event.key==pygame.K_DOWN or event.key == ord('s'):
                p_deltay=0

    pex+=p_deltax
    pey+=p_deltay
    screen.fill(negro)
    #screen.blit(negro,[0,0])
    #hacer el contorno del cuadrado
    L1P = pygame.draw.rect(screen2, warning, (0, 0, 800, ancho))
    L2P = pygame.draw.rect(screen2, warning, (0, 590, 800, ancho))
    A1P = pygame.draw.rect(screen2, warning, (790, 0, ancho, 800))
    A2P = pygame.draw.rect(screen2, warning, (0, 0, ancho, 800))

    #lineas
    obs1 = pygame.draw.rect(screen2, blanco, (px-72, 200, largo + 250, ancho))
    obs2 = pygame.draw.rect(screen2, blanco, (130, 10, ancho, 150))
    obs3 = pygame.draw.rect(screen2, blanco, (130, 204, ancho, 200))
    obs4 = pygame.draw.rect(screen2, blanco, (130, 440, ancho, 115))
    obs5 = pygame.draw.rect(screen2, blanco, (10, 501, largo-180, ancho))
    obs6 = pygame.draw.rect(screen2, blanco, (130, 550, 415, ancho))
    obs7 = pygame.draw.rect(screen2, blanco, (590, 10, ancho, 580))
    obs8 = pygame.draw.rect(screen2, blanco, (190, 501, 400, ancho))#vertical-
    obs30 = pygame.draw.rect(screen2, blanco, (370, 245, ancho, 165))#horizontal|
    obs10 = pygame.draw.rect(screen2, blanco, (380, 295, 160, ancho))#1sicksack
    obs11 = pygame.draw.rect(screen2, blanco, (430, 245, 160, ancho))#2
    obs12 = pygame.draw.rect(screen2, blanco, (430, 350, 160, ancho))  # 4sicksack
    obs13 = pygame.draw.rect(screen2, blanco, (300, 340, 80, ancho))  # 5
    obs14 = pygame.draw.rect(screen2, blanco, (285, 245, 85, ancho))  # 6sicksack
    obs15 = pygame.draw.rect(screen2, blanco, (130, 245, 105, ancho))  # vertical-
    obs16 = pygame.draw.rect(screen2, blanco, (180, 295, 105, ancho))  # vertical-
    obs17 = pygame.draw.rect(screen2, blanco, (130, 350, 105, ancho))  # vertical-
    obs18 = pygame.draw.rect(screen2, blanco, (130, 400, 65, ancho))  # vertical-
    obs19 = pygame.draw.rect(screen2, blanco, (235, 400, 310, ancho))  # vertical-
    obs20 = pygame.draw.rect(screen2, blanco, (235, 400, ancho, 50))  # horizontal|
    obs21 = pygame.draw.rect(screen2, blanco, (130, 440, 110, ancho))  # vertical-
    obs22 = pygame.draw.rect(screen2, blanco, (370, 450, ancho, 55))  # horizontal|
    obs23 = pygame.draw.rect(screen2, blanco, (290, 440, 90, ancho))  # vertical-
    obs24 = pygame.draw.rect(screen2, blanco, (420, 400, ancho, 60))  # horizontal|
    obs25 = pygame.draw.rect(screen2, blanco, (420, 450, 90, ancho))  # vertical-
    obs26 = pygame.draw.rect(screen2, blanco, (567, 441, 32, ancho))  # vertical-
    obs27 = pygame.draw.rect(screen2, blanco, (335, 295, 50, ancho))  # vertical-
    obs28 = pygame.draw.rect(screen2, blanco, (50, 400, 80, ancho))  # vertical-
    obs31 = pygame.draw.rect(screen2, blanco, (50, 400, ancho, 63))  # horizontal|
    obs29 = pygame.draw.rect(screen2, blanco, (10, 350, 85, ancho))  # vertical-
    obs32 = pygame.draw.rect(screen2, blanco, (89, 200, 6, 100))  # horizontal|
    obs33 = pygame.draw.rect(screen2, blanco, (48, 250, 6, 100))  # horizontal|
    obs34 = pygame.draw.rect(screen2, blanco, (48, 150, 6, 50))  # horizontal|
    obs35 = pygame.draw.rect(screen2, blanco, (89, 60, 6, 160))  # horizontal|
    obs36 = pygame.draw.rect(screen2, blanco, (10, 100, 15, ancho))  # vertical-
    obs37 = pygame.draw.rect(screen2, blanco, (65, 100, 24, ancho))  # vertical-
    obs38 = pygame.draw.rect(screen2, blanco, (50, 50, 45, ancho))  # vertical-
    obs39 = pygame.draw.rect(screen2, blanco, (185, 50, 320, ancho))  # vertical-
    obs40 = pygame.draw.rect(screen2, blanco, (490, 105, 100, ancho))  # vertical-
    obs41 = pygame.draw.rect(screen2, blanco, (484, 60, ancho, 55))  # horizontal|
    obs42 = pygame.draw.rect(screen2, blanco, (190, 150, 155, ancho))  # vertical-
    obs43 = pygame.draw.rect(screen2, blanco, (300, 150, ancho, 55))  # horizontal|
    obs44 = pygame.draw.rect(screen2, blanco, (140, 100, 292, ancho))  # vertical-
    obs45 = pygame.draw.rect(screen2, blanco, (400, 150, 140, ancho))  # vertical-
    obs46 = pygame.draw.rect(screen2, blanco, (400, 100, ancho, 55))  # horizontal|
    obs9 = pygame.draw.rect(screen, rojo, (x-210, 10, 100, 100))


    pelota = pygame.draw.circle(screen, rosa, (pex, pey), rp)
    if pelota.colliderect(obs1) or pelota.colliderect(obs2) or pelota.colliderect(obs3) or pelota.colliderect(obs4) or pelota.colliderect(obs5)  or pelota.colliderect(obs6) or pelota.colliderect(obs7) or pelota.colliderect(obs8) or pelota.colliderect(obs30) or pelota.colliderect(obs10) or pelota.colliderect(obs11) or pelota.colliderect(obs12) or pelota.colliderect(obs13) or pelota.colliderect(obs14) or pelota.colliderect(obs15) or pelota.colliderect(obs16) or pelota.colliderect(obs17) or pelota.colliderect(obs18) or pelota.colliderect(obs19) or pelota.colliderect(obs20) or pelota.colliderect(obs21) or pelota.colliderect(obs22) or pelota.colliderect(obs23) or pelota.colliderect(obs24) or pelota.colliderect(obs25) or pelota.colliderect(obs26) or pelota.colliderect(obs27) or pelota.colliderect(obs28) or pelota.colliderect(obs29) or pelota.colliderect(obs30) or pelota.colliderect(obs31) or pelota.colliderect(obs32) or pelota.colliderect(obs33) or pelota.colliderect(obs34) or pelota.colliderect(obs35) or pelota.colliderect(obs36) or pelota.colliderect(obs37) or pelota.colliderect(obs38) or pelota.colliderect(obs39) or pelota.colliderect(obs40) or pelota.colliderect(obs41) or pelota.colliderect(obs42) or pelota.colliderect(obs43) or pelota.colliderect(obs44) or pelota.colliderect(obs45) or pelota.colliderect(obs46) or pelota.colliderect(L2P) or pelota.colliderect(L1P) or pelota.colliderect(A2P) or pelota.colliderect(A1P):
        pex=pix
        pey=piy
    if pelota.colliderect(obs9):
        pygame.mixer.Sound.play(sonido_fondo)
        mx=10
        my=501
        px=150
        py=200
        cx=490
        cy=50
        radio=165
        x=200
        y=500
        ancho=13
        largo=280
        pix=490
        piy=30
        screen.fill(negro)
        screen.blit(fondo, [0, 0])
        fondo=pygame.image.load('negro.jpeg').convert()
        obs1 = pygame.draw.rect(screen2, rojo, (px, 80, largo + 400, ancho))
        obs9 = pygame.draw.rect(screen2, aqua, (x, y, 150, 150))

    if pelota.colliderect(obs9):
        pygame.mixer.Sound.stop(sonido_fondo)
        while (captura.isOpened()):
            ret, imagen = captura.read()
            if ret == True:
                cv2.imshow('video', imagen)
                pygame.mixer.Sound.play(pygame.mixer.Sound("tuaudio.wav"))
                if cv2.waitKey(100) == ord('s'):
                    break
            else:
                break
        captura.release()
        cv2.destroyAllWindows()
    pygame.display.flip()
    clok.tick(50)
