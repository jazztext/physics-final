#!/usr/bin/env python

# Libraries!
import pygame
import pygame.gfxdraw
import cmath
import sys
import random
import argparse


# Command line options (really just for experimentation)
parser=argparse.ArgumentParser(description="Julia set generator")
parser.add_argument("-w", "--width", type=int, 
	help="set window width to WIDTH", metavar="WIDTH", default=1000)
parser.add_argument("-H", "--height", type=int, 
	help="set window height to HEIGHT", metavar="HEIGHT", default=750)
parser.add_argument("-m", "--mode", type=str, 
	help="change mode (pixel,line,full)", metavar="MODE", default="line")
# Unless otherwise specified, c will be given a random value consisting
# of a real part between -1 and 1 and an imaginary part between -1 and 1
parser.add_argument("-r", "--real", type=float,
	help="set real part of c", metavar="REAL", default=random.uniform(-1,1))
parser.add_argument("-i", "--imaginary", type=float, 
	help="set imaginary part of c", metavar="IMAG", default=random.uniform(-1,1))
args=parser.parse_args()
width=args.width
height=args.height
mode=args.mode
c=complex(args.real,args.imaginary)
print "Using",c,"as c value"

# Set up window grid
if width>height:
	ppu=width/3.5
elif height>width:
	ppu=height/3.5
else:
	ppu=width/3.5

# Declaration of variables, values at this point are unimportant
x=0
y=0
n=0+0j

# Process previous command line options
# Decides frequency of screen updates, default is when a line is completed
if (mode=="pixel"):
	q=1
elif (mode=="full"):
	q=3
else:
	q=2


# The function that will be iterated through, usually it should just be n*n
def f(n):
	n=n*n
	return n

# Color processing, makes a fairly steady gradient
# Change the positioning of the "255-5*i" statements
# For different colored gradients, but I prefer teal to black
def colortest(i):
	if (i<=50):
		return (0,255-5*i,255-5*i)
	else:
		return (0,0,0)


# Actual calculations! 
# Due to multiple conditions, a while statement is preferable to a for
# Also the escape conditions of a julia or mandelbrot set state when the
# distance from the origin is >2, it will become infinitely large
def julia(n):
	i=0
	while ((((n.real*n.real)+(n.imag*n.imag))**0.5)<2) and (i<51):
		n=f(n)+c
		i+=1
	return colortest(i)

def keep():
	# Keep the window open until the close signal is given
	running=True
	while running:
		pass
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False


def main():
	# Initialize display
	screen=pygame.display.set_mode((int(width),int(height)))
	
	# Main process, processes by rows then columns
	for y in range(0,height):
		for x in range(0,width):
			n=complex(x-width/2,y-height/2)
			pygame.gfxdraw.pixel(screen,x,y,julia(n/ppu))
			# If user selected pixel mode, update after calculating each pixel
			if (q==1):
				pygame.display.flip()
		# If user selected line mode, update after calculating each line
		if (q==2):
			pygame.display.flip()
	# If user selected full mode, wait until all values are calculated
	# then show the completed fractal
	if (q==3):
		pygame.display.flip()
	keep()

# Parts of the program that actually run!
main()





