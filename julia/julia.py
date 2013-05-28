#!/usr/bin/env python

#width=0
#height=0
#mode="line"
#width="1000"
#height="750"
#mode="line"

import pygame
import pygame.gfxdraw
import cmath
import sys
import random
import argparse

parser=argparse.ArgumentParser(description="Julia set generator")


#parser=OptionParser()
#parser.set_default(width,1000)
#parser.set_default(height,750)
#arser.set_default(mode,"line")
#parser.set_defualts(height=750)
#parser.set_defaults(mode="line")

parser.add_argument("-w", "--width", type=int, help="set window width to WIDTH", metavar="WIDTH", default=1000)
parser.add_argument("-H", "--height", type=int, help="set window height to HEIGHT", metavar="HEIGHT", default=750)
parser.add_argument("-m", "--mode", type=str, help="change mode (pixel,line,full)", metavar="MODE", default="line")
parser.add_argument("-r", "--real", type=float, help="set real part of c", metavar="REAL", default=random.uniform(-1,1))
parser.add_argument("-i", "--imaginary", type=float, help="set imaginary part of c", metavar="IMAG", default=random.uniform(-1,1))

args=parser.parse_args()
width=args.width
height=args.height
mode=args.mode
c=complex(args.real,args.imaginary)

if width>height:
	ppu=width/2.5
elif height>width:
	ppu=height/2.5
else:
	ppu=width/2.5

x=0
y=0

if (mode=="pixel"):
	q=1
elif (mode=="full"):
	q=3
else:
	q=2

#r=raw_input("Real part of c: ")
#if (r=="random"):
	#r=random.uniform(-1,1)
	#print "Using ",r," as real part of c"

#i=raw_input("Imaginary part of c: ")
#if (i=="random"):
#	i=random.uniform(-1,1)
	#print "Using ",i," as imaginary part of c"

#c=complex(float(r),float(i))

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

screen=pygame.display.set_mode((int(width),int(height)))
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



