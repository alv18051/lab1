#Libreria de graficos
 

import struct #esta libreria si se puede usar
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    #4 bytes
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Renderer(object):
    #INICIALIZADOR
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.clearColor = color(0,0,0)
        self.currentColor = color(1,1,1)

        self.glViewport(0,0,self.width,self.height)

        self.glClear()

    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor (self, r, g, b): 
       
        self.currentColor = color(r,g,b)


#funcion para borrar todos los pixeles y crear el array de pixeles.
    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)] for x in range(self.width)]

#funcion para crear limpiar el viewport
    def glClearViewport(self, clr = None):
        for x in range(self.vpX, self.vpX + self.vpWidth):
            for y in range(self.vpY, self.vpY + self.vpHeight):
                self.glPixel(x, y, clr)

#funcion para dibujar un pixel
    def glPixel(self, x, y, clr = None):
         if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor 

#funcion para el viewport
    def glViewport(self, posX,posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

        self.viewport = (posX, posY, width, height)

#funcion de dibuajr un pixel en el viewport
    def glPixelViewport(self, x, y, clr = None):
        x = (x + 1) * (self.vpWidth / 2) + self.vpX
        y = (y + 1) * (self.vpHeight / 2) + self.vpY
        x = int(x)
        y = int(y)
        self.glPixel(x , y , clr)

#funcion para las lineas
    def glLine(self, v0, v1, clr = None):
        #Bresenham line algorithm

        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        if x0 == x1 and y0 == y1:
            self.glPixel(x0, y0, clr )
            return

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0 

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5

        m = dy/dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                self.glPixel(y, x, clr)
            else:
                self.glPixel(x, y, clr)

            offset += m
            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1
            
        #algoritmo inicial de las lineas
        # m = dy / dx

        # y = y0

        # for x in range(x0, x1 + 1):
        #     y += m
        #     y = int(y)
        #     self.glPixel(x, y, clr)


    def glTriangle(self, A, B, C, color = None):

        if A.y < B.y:
            A, B = B, A
        if A.y < C.y:
            A, C = C, A
        if B.y < C.y:
            B, C = C, B

        try:
            d_31 = (C.x - A.x) / (C.y - A.y)
            d_32 = (C.x - A.x) / (C.y - B.y)
        except:
            pass
        else:
            x1 = C.x
            x2 = C.x

            for y in range(C.y, A.y + 1):
                self.glLine(V2(int(A),y), V2(int(B),y), color)
                x1 += d_31
                x2 += d_32
        


#funcion para poder abrir el archivo con un visualizador o crear la imagen. 
    def glFinish(self, filename):
        with open(filename, "wb") as file: 
            #header o encabezado de la imagen
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14+40+(self.width * self.height*3)))
            file.write(dword(0))
            file.write(dword(14+40))

            #infoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.height*self.width*3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #colortable
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
    



    
        
    
