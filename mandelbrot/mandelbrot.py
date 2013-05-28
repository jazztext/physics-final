#!/usr/bin/env python

import pygame
import pygame.gfxdraw
import cmath

width=1000
height=750
ppu=280

x=0
y=0
c=0.25+0.5j

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


def mandel(n):
	i=0
	z=0+0j
	while ((((z.real*z.real)+(z.imag*z.imag))**0.5)<2) and (i<50):
		z=f(z)+n
		i+=1
	return colortest(i)

screen=pygame.display.set_mode((width,height))

clock=pygame.time.Clock()
running=True

while running:
	n=0+0j
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-3*width/4,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,mandel(n/ppu))
		pygame.display.flip()
	clock.tick(240)
	running=False
while True:
	pygame.display.flip()
    




