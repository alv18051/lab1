#Programa principal
import random
from gl import *
alto = 960  #alto de la pantalla
ancho = 540 #ancho de la pantalla
rende = Renderer(alto,ancho)

rende.glClearColor(1,1,1)
rende.glColor(0,0,0)

rende.glClear()

poligono1 = [V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345), V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385), V2(205, 410), V2(193, 383)]

for i in range(len(poligono1)):
    rende.glLine(poligono1[i], poligono1[(i+1) % len(poligono1)])

poligono2 = [V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302)]

for i in range(len(poligono2)):
    rende.glLine(poligono2[i], poligono2[(i+1) % len(poligono2)])

poligono3 = [V2(377, 249), V2(411, 197), V2(436, 249)]

for i in range(len(poligono3)):
    rende.glLine(poligono3[i], poligono3[(i+1) % len(poligono3)])

poligono4 = [V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52), V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180)]

for i in range(len(poligono4)):
    rende.glLine(poligono4[i], poligono4[(i+1) % len(poligono4)])

poligono5 = [V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170)]

for i in range(len(poligono5)):
    rende.glLine(poligono5[i], poligono5[(i+1) % len(poligono5)])



#1
rende.glColor(1,1,0)
A,B,C = V2(377, 249), V2(411, 197), V2(436, 249)
rende.glTriangle(A,B,C)

#2
rende.glColor(1,0.5,0)
A,B,C= V2(321,335), V2(288,286), V2(374,302)
rende.glTriangle(A, B, C)
A,B,C= V2(288,286), V2(374,302), V2(339, 251)
rende.glTriangle(A, B, C)

#3
rende.glColor(0,1,1)
A,B,C= V2(207, 345), V2(180, 330), V2(185, 360)
rende.glTriangle(A, B, C)
A,B,C= V2(220, 385), V2(250, 380), V2(230, 360)
rende.glTriangle(A, B, C)
A,B,C= V2(165,380), V2(185,360), V2(193,383)
rende.glTriangle(A, B, C)
A,B,C= V2(193, 383), V2(220, 385), V2(205, 410)
rende.glTriangle(A, B, C)
A,B,C= V2(230, 360), V2(233, 330), V2(207, 345)
rende.glTriangle(A, B, C)
A,B,C= V2(193, 383), V2(207, 345), V2(185, 360)
rende.glTriangle(A, B, C)
A,B,C= V2(193, 383), V2(230, 360), V2(207, 345)
rende.glTriangle(A, B, C)
A,B,C= V2(193, 383), V2(220, 385), V2(230, 360)
rende.glTriangle(A, B, C)

#4
rende.glColor(0,1,0.66)
A,B,C= V2(597, 215), V2(580, 230), V2(615, 214)
rende.glTriangle(A, B, C)
A,B,C= V2(750, 145), V2(761, 179), V2(672, 192)
rende.glTriangle(A, B, C)
A,B,C= V2(750, 145), V2(672, 192), V2(660, 52)
rende.glTriangle(A, B, C)
A,B,C= V2(502, 88), V2(448, 159), V2(466, 180)
rende.glTriangle(A, B, C)
A,B,C= V2(502, 88), V2(517, 144), V2(466, 180)
rende.glTriangle(A, B, C)
A,B,C= V2(660, 52), V2(517, 144), V2(553, 53)
rende.glTriangle(A, B, C)
A,B,C= V2(660, 52), V2(517, 144), V2(552, 214)
rende.glTriangle(A, B, C)
A,B,C= V2(660, 52), V2(659, 214), V2(552, 214)
rende.glTriangle(A, B, C)
A,B,C= V2(660, 52), V2(659, 214), V2(672, 192)
rende.glTriangle(A, B, C)
A,B,C= V2(632, 230), V2(580, 230), V2(615, 214)
rende.glTriangle(A, B, C)
A,B,C= V2(413, 177), V2(448, 159), V2(466, 180)
rende.glTriangle(A, B, C)
A,B,C= V2(502, 88), V2(517, 144), V2(553, 53)
rende.glTriangle(A, B, C)
A,B,C= V2(660, 52), V2(676, 37), V2(553, 53)
rende.glTriangle(A, B, C)
A,B,C= V2(535, 36), V2(676, 37), V2(553, 53)
rende.glTriangle(A, B, C)
rende.glColor(1,1,1)
A,B,C= V2(682, 175), V2(735, 148), V2(739, 170)
rende.glTriangle(A, B, C)
A,B,C= V2(682, 175), V2(735, 148), V2(708, 120)
rende.glTriangle(A, B, C)

    


rende.glFinish("./salida.bmp")