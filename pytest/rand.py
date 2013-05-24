#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import cmath
import sys
import random

width=800
height=780
ppu=300

x=0
y=0
r=random.uniform(-1,1)
#print "Using ",r," as real part of c"
i=random.uniform(-1,1)
#print "Using ",i," as imaginary part of c"
c=complex(r,i)

def f(n):
	n=n*n
	return n

def colortest(i):
	if (i<=10):
		return (0,255-5*i,255-5*i)
	elif (i<=50):
		return (0,255-5*i,255-5*i)
	#elif (i<=20):
	#	return (0,255-5*i,0)
	#elif (i<=255):
	#	return (255-i,255-i,255-i)
	#elif (i>50):
	else:
		return (0,0,0)
	#return (0,0,255-i)


def julia(n,c):
	i=0
	while ((((n.real*n.real)+(n.imag*n.imag))**0.5)<2) and (i<51):
		n=f(n)+c
		i+=1
	return colortest(i)

def main():
	print "-----------------------------------------------"
	r=random.uniform(-1,1)
	print "Using ",r," as real part of c"
	i=random.uniform(-1,1)
	print "Using ",i," as imaginary part of c"
	c=complex(r,i)
	screen=pygame.display.set_mode((width,height))

	clock=pygame.time.Clock()
	running=True

	while running:
		n=0+0j
		for y in range(0,height):
			for x in range(0,width):
				n=complex(x-width/2,y-height/2)
				pygame.gfxdraw.pixel(screen,x,y,julia(n/ppu,c))
			pygame.display.flip()
		clock.tick(240)
		running=False
while True:
	main()
    




