# mandelbrot.py
# Lab 9
#
# Name: Luke McEvoy
#I pledge my honor that I have abided by the Stevens Honor System

from cs5png import *
import turtle

#For loop addition that leads to multiplication
def mult( c, n ):
    result = 0
    for x in range(n):
        result = c + result
    return result

#starts z=0, runs z**2 + c for n times
def update(c,n):
    z = 0
    for n in range(n):
        z = z**2 + c
    return z

#complex and integer, boolean if in Mandelbrot set
def inmset(c,n):
    z = 0
    for n in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

#returns false if abs(z)>2, true if never greater than 2
def weWantThisPixel( col, row ):
    if col%10 == 0 and row%10 == 0:
#or makes grid bc one condition is always x%10 = 0
        return True
    else:
        return False

def test():
    width = 300
    height = 200
    image = PNGImage(width, height)
# create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
# we looped through every image pixel; we now write the file
    image.saveFile()

def scale(pix,pixMax,floatMin,floatMax):
    
    return floatMin + (1.0*pix/pixMax) * (floatMax - floatMin)

def test():
    width = 300
    height = 200
    image = PNGImage(width, height)
# create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
# we looped through every image pixel; we now write the file
    image.saveFile()

#png mandelbrot returned in file update
def mset():
    width=300
    height=200
    image=PNGImage(width,height)
    for col in range(width):
        x = (scale(col,width, -2.0, 1.0))
        for row in range(height):
            y = (scale(row, height, -1.0, 1.0))
            c = x + y*1j
            if inmset(c,25):
                image.plotPoint(col, row)
    image.saveFile()

print(mult(3,4))
print(update(-1,3))
c = 3+4*1j
print(inmset(c,25))
print(scale(100,300,-2,1))

mset()
