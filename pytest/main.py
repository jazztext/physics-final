#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import cmath
import sys
import random

width=1000
height=750
ppu=280

x=0
y=0

print "Welcome to Julia Set Generator!"
print "Available modes: slow, medium (default), fast"
m=raw_input("Mode: ")
if (m=="slow"):
	q=1
elif (m=="fast"):
	q=3
else:
	q=2

r=raw_input("Real part of c: ")
if (r=="random"):
	r=random.uniform(-1,1)
	print "Using ",r," as real part of c"

i=raw_input("Imaginary part of c: ")
if (i=="random"):
	i=random.uniform(-1,1)
	print "Using ",i," as imaginary part of c"

c=complex(float(r),float(i))

def f(n):
	n=n*n
	return n

def colortest(i):
	if (i<=10):
		return (0,255-5*i,255-5*i)
	elif (i<=50):
		return (0,255-5*i,255-5*i)
	else:
		return (0,0,0)



def julia(n):
	i=0
	while ((((n.real*n.real)+(n.imag*n.imag))**0.5)<2) and (i<255):
		n=f(n)+c
		i+=1
	return colortest(i)

screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
running=True

while running:
	n=0+0j
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-width/2,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,julia(n/ppu))
			if (q==1):
				pygame.display.flip()
		if (q==2):
			pygame.display.flip()
	clock.tick(240)
	running=False
	if (q==3):
		pygame.display.flip()

while True:
	pygame.display.flip()



